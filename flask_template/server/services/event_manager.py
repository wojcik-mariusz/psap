from typing import NoReturn
from datetime import datetime

from typing import NoReturn, List
from datetime import datetime

from flask_template.db.db_tools import Event

from sqlalchemy import and_, delete


def insert_new_event(**kwargs):
    pass


def delete_event(event_id: int) -> NoReturn:
    pass


def get_all_list_event() -> List[str]:
    pass


def get_active_paramedic_list_event() -> List[str]:
    pass


def get_active_police_list_event() -> List[str]:
    pass


def get_active_fire_service_event() -> List[str]:
    pass
