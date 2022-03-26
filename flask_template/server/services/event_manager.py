from typing import NoReturn, List
from datetime import datetime

from flask_template.db.db_tools import Events


def chose_duty(list_of_emergency_services_needed: List[int]):
    print(list_of_emergency_services_needed[0])
    print(type(list_of_emergency_services_needed[0]))
    chose_duty = {1: "fw_to_fire_service", 2: "fw_to_police", 3: "fw_to_paramedic"}
            # fw_to_fire_service: True
    print({chose_duty[list_of_emergency_services_needed[0]]: True})
    print({f"{chose_duty[list_of_emergency_services_needed[0]]}": True})
    return {f"{chose_duty[list_of_emergency_services_needed[0]]}": True}

def insert_new_event(**kwargs) -> NoReturn:
    """TODD in Sphinx format"""
    emergency = chose_duty(kwargs["list_of_emergency_services_needed"])
    print(emergency)
    return Events(event_date=datetime.now, **emergency, **kwargs)


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
