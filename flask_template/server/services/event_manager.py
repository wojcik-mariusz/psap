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


#
#
def get_paramedic_list_event() -> List[str]:
    paramedic_event_list = Events.query.filter(
        and_(Events.street == "Polna", Events.street_number == "3")).first()
    return paramedic_event_list
#
#
# def get_police_list_event()-> List[str]:
#     police_event_list = Events.query.filter_by(fw_to_police='True').all()
#     return police_event_list
#
#
# def get_fire_service_list_event()-> List[str]:
#     fire_service_event_list = Events.query.filter_by(Events.fw_to_fire_service == 'True').all()
#     return fire_service_event_list
