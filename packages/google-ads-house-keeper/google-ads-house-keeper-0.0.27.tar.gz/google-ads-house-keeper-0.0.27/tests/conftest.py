from typing import List

from datetime import datetime
from googleads_housekeeper.adapters import repository
from googleads_housekeeper.domain import events, task
from googleads_housekeeper.services import unit_of_work, external_parsers
import pytest


class FakeRepository(repository.AbstractRepository):

    def __init__(self):
        super().__init__()
        self.session = list()

    def _add(self, element):
        self.session.append(element)

    def _get(self, task_id):
        return next(e for e in self.session if e.id == task_id)

    def _get_by_condition(self, entity_name, condition_value):
        try:
            return next(e for e in self.session
                        if getattr(e, entity_name) == condition_value)
        except StopIteration:
            return None

    def _list(self):
        return list(self.session)

    def _update(self, task_id, update_dict):
        element = self._get(task_id)
        element_dict = element.__dict__
        element_dict.update(update_dict)
        element.__init__(**element_dict)

    def _delete(self, task_id):
        element = self._get(task_id)
        self.session.remove(element)


class FakeUnitOfWork(unit_of_work.AbstractUnitOfWork):
    tasks: FakeRepository = FakeRepository()
    settings: FakeRepository = FakeRepository()
    customer_ids: FakeRepository = FakeRepository()
    mcc_ids: FakeRepository = FakeRepository()
    website_info: FakeRepository = FakeRepository()
    youtube_channel_info: FakeRepository = FakeRepository()
    youtube_video_info: FakeRepository = FakeRepository()
    allowlisting: FakeRepository = FakeRepository()
    executions: FakeRepository = FakeRepository()
    execution_details: FakeRepository = FakeRepository()
    published_events: List[events.Event] = []

    def __init__(self) -> None:
        ...

    def _commit(self):
        self.committed = True

    def rollback(self):
        ...

@pytest.fixture
def uow(): 
    return FakeUnitOfWork()
