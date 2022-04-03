from typing import NoReturn
from datetime import datetime

from typing import NoReturn, List
from datetime import datetime

from flask_template.db.db_tools import Events

from sqlalchemy import and_


def insert_new_event(**kwargs) -> NoReturn:
    """TODD in Sphinx format"""
    return Events(event_date=datetime.now(), **kwargs)


def get_all_list_event() -> List[str]:
    return Events.query.all()


def get_paramedic_list_event() -> List[str]:
    paramedic_event_list = Events.query.filter(and_(Events.fw_to_paramedic == "1", Events.archived == "0")).all()
    return paramedic_event_list
