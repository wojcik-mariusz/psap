from typing import NoReturn
from datetime import datetime

from flask_template.db.db_tools import Events


def insert_new_event(**kwargs) -> NoReturn:
    """TODD in Sphinx format"""
    return Events(event_date=datetime.now(), **kwargs)


# def get_all_list_event() -> List[str]:
#     event_list = Events.query.order_by(Events.id).all()
#     return event_list
#
#
# def get_paramedic_list_event()-> List[str]:
#     paramedic_event_list = Events.query.filter(and_(fw_to_paramedic='True', archived='False'))
#     return paramedic_event_list
#
#
# def get_police_list_event()-> List[str]:
#     police_event_list = Events.query.filter_by(fw_to_police='True').all()
#     return police_event_list
#
#
# def get_fire_service_list_event()-> List[str]:
#     fire_service_event_list = Events.query.filter_by(fw_to_fire_service='True').all()
#     return fire_service_event_list
