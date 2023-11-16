# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import annotations
from collections.abc import Sequence

from typing import Any, Dict, Callable, List, Optional, Tuple
from dataclasses import asdict
from datetime import datetime, timedelta
from functools import reduce
import logging
import json
from operator import add
import pickle
import sqlalchemy

from gaarf.api_clients import GoogleAdsApiClient
from gaarf.report import GaarfReport
from gaarf.query_executor import AdsReportFetcher

from googleads_housekeeper.domain import allowlisting, commands, events, execution, settings, task
from googleads_housekeeper.domain.placements import Placements, PlacementsConversionSplit, aggregate_placements, join_conversion_split
from googleads_housekeeper.adapters import notifications, publisher

from . import unit_of_work
from .exclusion_service import PlacementExcluder
from .rules_parser import RulesParser
from .enums import ExclusionTypeEnum, ExclusionLevelEnum
from .exclusion_specification import BaseExclusionSpecification, Specification


def get_accessible_mcc_ids(cmd: commands.GetMccIds,
                           uow: unit_of_work.AbstractUnitOfWork,
                           ads_api_client: GoogleAdsApiClient) -> List[str]:
    api_client = ads_api_client.client
    customer_service = api_client.get_service("CustomerService")
    accessible_customers = customer_service.list_accessible_customers()
    mcc_ids = [
        resource.split('/')[1]
        for resource in accessible_customers.resource_names
    ]
    mcc_full = []
    for mcc in mcc_ids:
        report_fetcher = AdsReportFetcher(api_client=ads_api_client,
                                          customer_ids=mcc)
        try:
            mcc_data = report_fetcher.fetch("""
            SELECT
                customer_client.descriptive_name AS account_name,
                customer_client.id AS account_id
            FROM customer_client
            WHERE customer_client.manager = TRUE
            AND customer_client.status = "ENABLED"
            """)
            if mcc_data:
                mcc_full.append(mcc_data)
        except Exception:
            pass
    with uow:
        for mcc in mcc_full:
            for row in mcc:
                uow.mcc_ids.add(
                    settings.MccIds(mcc_id=row.account_id,
                                    account_name=row.account_name))
        try:
            uow.commit()
        except sqlalchemy.exc.IntegrityError:
            pass
    return mcc_ids


def get_customer_ids(
        cmd: commands.GetMccIds, uow: unit_of_work.AbstractUnitOfWork,
        ads_api_client: GoogleAdsApiClient) -> List[Dict[str, int]]:
    report_fetcher = AdsReportFetcher(api_client=ads_api_client,
                                      customer_ids=cmd.mcc_id)
    customer_ids = report_fetcher.fetch("""
    SELECT
        customer_client.descriptive_name AS account_name,
        customer_client.id AS customer_id
    FROM customer_client
    WHERE customer_client.manager = FALSE
    AND customer_client.status = "ENABLED"
    """)
    result = []
    with uow:
        for account_name, customer_id in customer_ids:
            result.append({"account_name": account_name, "id": customer_id})
            uow.customer_ids.add(
                settings.CustomerIds(mcc_id=cmd.mcc_id,
                                     account_name=account_name,
                                     id=customer_id))
        try:
            uow.commit()
        except sqlalchemy.exc.IntegrityError:
            pass
    return result


def run_manual_exclusion_task(cmd: commands.RunManualExclusion,
                              uow: unit_of_work.AbstractUnitOfWork,
                              ads_api_client: GoogleAdsApiClient):
    with uow:
        placement_excluder = PlacementExcluder(ads_api_client, uow)
        placement_excluder.exclude_placements(
            GaarfReport(results=cmd.placements, column_names=cmd.header))


def task_created(event: events.TaskCreated,
                 publisher: publisher.BasePublisher) -> None:
    publisher.publish("task_created", event)


def task_updated(event: events.TaskUpdated,
                 publisher: publisher.BasePublisher) -> None:
    publisher.publish("task_updated", event)


def task_deleted(event: events.TaskDeleted,
                 publisher: publisher.BasePublisher) -> None:
    publisher.publish("task_deleted", event)


def run_task(
        cmd: commands.RunTask,
        uow: unit_of_work.AbstractUnitOfWork,
        ads_api_client: GoogleAdsApiClient,
        notification_service: Optional[notifications.BaseNotifications] = None,
        save_to_db: bool = True):
    with uow:
        task_obj = uow.tasks.get(task_id=cmd.id)
        report_fetcher = AdsReportFetcher(api_client=ads_api_client)
        exclusion_specification = RulesParser().generate_specifications(
            task_obj.exclusion_rule)
        placement_excluder = PlacementExcluder(ads_api_client, uow)
        specification = Specification(uow)
        start_time = datetime.now()
        to_be_excluded_placements = find_placements_for_exclusion(
            task_obj, report_fetcher, specification, exclusion_specification)
        if notification_service and task_obj.output in (
                task.TaskOutput.NOTIFY, task.TaskOutput.EXCLUDE_AND_NOTIFY):
            if to_be_excluded_placements:
                message_body = to_be_excluded_placements[[
                    "placement_type", "name"
                ]].to_pandas()
            else:
                message_body = "no placements were excluded"
            notification_service.send(message_body=message_body,
                                      title=task_obj.name,
                                      custom_sender=task_obj.name)

        if to_be_excluded_placements and task_obj.output in (
                task.TaskOutput.EXCLUDE, task.TaskOutput.EXCLUDE_AND_NOTIFY):
            placement_excluder.exclude_placements(to_be_excluded_placements,
                                                  task_obj.exclusion_level)

            end_time = datetime.now()
            execution_obj = execution.Execution(task=cmd.id,
                                                start_time=start_time,
                                                end_time=end_time)
            uow.executions.add(execution_obj)
            if save_to_db:
                for placement in to_be_excluded_placements:
                    if hasattr(placement, "reason"):
                        exclusion_reason = placement.reason
                    else:
                        exclusion_reason = ""
                    uow.execution_details.add(
                        execution.ExecutionDetails(
                            execution_id=execution_obj.id,
                            placement=placement.name,
                            placement_type=placement.placement_type,
                            reason=exclusion_reason))
            uow.commit()


def preview_placements(cmd: commands.PreviewPlacements,
                       uow: unit_of_work.AbstractUnitOfWork,
                       ads_api_client: GoogleAdsApiClient,
                       save_to_db: bool = True) -> Dict[str, Any]:
    report_fetcher = AdsReportFetcher(api_client=ads_api_client)
    placement_excluder = PlacementExcluder(ads_api_client, uow)
    exclusion_specification = RulesParser().generate_specifications(
        cmd.exclusion_rule)
    task_obj = task.Task(name="",
                         exclusion_rule=cmd.exclusion_rule,
                         customer_ids=cmd.customer_ids,
                         date_range=cmd.date_range,
                         from_days_ago=cmd.from_days_ago,
                         exclusion_level=cmd.exclusion_level,
                         placement_types=cmd.placement_types)
    specification = Specification(uow)
    to_be_excluded_placements = find_placements_for_exclusion(
        task_obj, report_fetcher, specification, exclusion_specification,
        save_to_db)
    if not to_be_excluded_placements:
        data = {}
    else:
        data = json.loads(
            to_be_excluded_placements.to_pandas().to_json(orient="index"))
    return {
        "data": data,
        "dates": {
            "date_from": task_obj.start_date,
            "date_to": task_obj.end_date
        }
    }


def find_placements_for_exclusion(
        task: task.Task,
        report_fetcher: AdsReportFetcher,
        specification: Specification,
        exclusion_specification: Optional[Sequence[
            Sequence[BaseExclusionSpecification]]],
        save_to_db: bool = True) -> GaarfReport | None:
    runtime_options = RulesParser().define_runtime_options(
        exclusion_specification)
    start_date, end_date = task.get_start_end_date()
    reports: list[GaarfReport] = []
    for account in task.accounts:
        placement_query = Placements(placement_types=task.placement_types,
                                     start_date=start_date,
                                     end_date=end_date)
        placements = report_fetcher.fetch(placement_query,
                                          customer_ids=account)
        if not placements:
            continue
        if runtime_options.is_conversion_query:
            conversion_split_query = PlacementsConversionSplit(
                placement_types=task.placement_types,
                start_date=start_date,
                end_date=end_date),
            if placements_by_conversion_name := report_fetcher.fetch(
                    conversion_split_query, customer_ids=account):
                placements_by_conversion_name = (
                    specification.apply_specifications(
                        [runtime_options.conversion_rules],
                        placements_by_conversion_name))
                placements = join_conversion_split(
                    placements, placements_by_conversion_name,
                    runtime_options.conversion_name)
            else:
                continue
        placements = aggregate_placements(placements, task.exclusion_level)
        if not exclusion_specification:
            for placement in placements:
                placement["reason"] = ""
            reports.append(placements)
            continue
        for rule in exclusion_specification:
            # Identify all ads and non_ads specifications
            ads_specs = [
                r for r in rule
                if r.exclusion_type == ExclusionTypeEnum.GOOGLE_ADS_INFO
            ]
            non_ads_specs = [
                r for r in rule
                if r.exclusion_type != ExclusionTypeEnum.GOOGLE_ADS_INFO
            ]

            # If we don't have any non_ads specification proceed to applying them
            if ads_specs and not non_ads_specs:
                continue
            # If we have a mix of ads and non_ads specifications apply ads first
            # and then parse non-ads ones
            elif ads_specs and non_ads_specs:
                to_be_parsed_placements = (specification.apply_specifications(
                    [ads_specs], placements))
                parse_via_external_parsers(to_be_parsed_placements,
                                           non_ads_specs, specification.uow,
                                           save_to_db)
            # If there are only non_ads specification proceed to applying them
            elif not ads_specs and non_ads_specs:
                parse_via_external_parsers(placements, non_ads_specs,
                                           specification.uow, save_to_db)

        if (to_be_excluded_placements :=
                specification.apply_specifications(exclusion_specification,
                                                   placements)):
            reports.append(to_be_excluded_placements)
    if reports:
        return reduce(add, reports)
    return None


def parse_via_external_parsers(
        to_be_parsed_placements: GaarfReport,
        non_ads_specs: Sequence[BaseExclusionSpecification],
        uow: unit_of_work.AbstractUnitOfWork,
        save_to_db: bool = True) -> None:
    with uow:
        for non_ads_spec_rule in non_ads_specs:
            for placement_info in to_be_parsed_placements:
                repo = getattr(uow, non_ads_spec_rule.repository_name)
                if (placement_info.placement_type ==
                        non_ads_spec_rule.corresponding_placement_type.name):

                    if not repo.get_by_condition("placement",
                                                 placement_info.name):
                        parsed_placement_info = non_ads_spec_rule.parser(
                        ).parse(placement_info.placement)
                        if save_to_db:
                            repo.add(parsed_placement_info)
        uow.commit()


def save_task(
    cmd: commands.SaveTask,
    uow: unit_of_work.AbstractUnitOfWork,
) -> str:
    with uow:
        task_id = None
        task_obj = None
        if hasattr(cmd, "task_id") and cmd.task_id:
            task_id = cmd.task_id
            task_obj = uow.tasks.get(task_id=task_id)
            update_dict = asdict(cmd)
            update_dict.pop("task_id")
            uow.tasks.update(task_obj.id, update_dict)
            uow.published_events.append(events.TaskUpdated(task_obj.id))
        else:
            task_dict = asdict(cmd)
            task_dict.pop("task_id")
            task_obj = task.Task(**task_dict)
            uow.tasks.add(task_obj)
            task_id = task_obj.id
            uow.published_events.append(events.TaskCreated(task_id))
        uow.commit()
        task_id = task_obj.id
        return str(task_id)


def delete_task(
    cmd: commands.DeleteTask,
    uow: unit_of_work.AbstractUnitOfWork,
):
    with uow:
        task_obj = uow.tasks.get(task_id=cmd.task_id)
        if task_obj:
            uow.tasks.update(cmd.task_id, {"status": "INACTIVE"})
            uow.commit()
            uow.published_events.append(events.TaskDeleted(cmd.task_id))
        else:
            logging.warning("No task with id %d found!", cmd.id)


def save_config(
    cmd: commands.SaveConfig,
    uow: unit_of_work.AbstractUnitOfWork,
):
    with uow:
        task_id = None
        task_obj = None
        if hasattr(cmd, "id") and cmd.id:
            config_id = cmd.id
            config = uow.settings.get(config_id)
            update_dict = asdict(cmd)
            update_dict.pop("id")
            uow.settings.update(config.id, update_dict)
        else:
            config_dict = asdict(cmd)
            config_dict.pop("id")
            config = settings.Config(**config_dict)
            uow.settings.add(config)
        uow.commit()


def add_to_allowlisting(cmd: commands.AddToAllowlisting,
                        uow: unit_of_work.AbstractUnitOfWork) -> None:
    with uow:
        placement = allowlisting.AllowlistedPlacement(
            cmd.placement.get("type"), cmd.placement.get("name"))
        if not uow.allowlisting.get_by_condition("name", placement.name):
            uow.allowlisting.add(placement)
            uow.commit()


def remove_from_allowlisting(cmd: commands.RemoveFromAllowlisting,
                             uow: unit_of_work.AbstractUnitOfWork) -> None:
    with uow:
        if allowlisted_placement := uow.allowlisting.get_by_condition(
                "name", cmd.placement.get("name")):
            uow.allowlisting.delete(allowlisted_placement.id)


EVENT_HANDLERS = {
    events.TaskCreated: [task_created],
    events.TaskUpdated: [task_updated],
    events.TaskDeleted: [task_deleted]
}

COMMAND_HANDLERS = {
    commands.RunTask: run_task,
    commands.SaveTask: save_task,
    commands.DeleteTask: delete_task,
    commands.RunManualExclusion: run_manual_exclusion_task,
    commands.PreviewPlacements: preview_placements,
    commands.SaveConfig: save_config,
    commands.GetCustomerIds: get_customer_ids,
    commands.GetMccIds: get_accessible_mcc_ids,
    commands.AddToAllowlisting: add_to_allowlisting,
    commands.RemoveFromAllowlisting: remove_from_allowlisting,
}
