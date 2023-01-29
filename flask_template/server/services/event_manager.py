from typing import NoReturn, List


from flask_template.db.db_tools import Event, EventService, DB


def get_event_by_id(event_id):
    return Event.query.filter(Event.id == event_id).first()


def get_all_list_event() -> List[str]:
    return Event.query.order_by(Event.event_date).all()


def get_active_paramedic_list_event() -> List[str]:
    return EventService.query.filter(EventService.fw_to_paramedic == 1).all()


def get_active_police_list_event() -> List[str]:
    return EventService.query.filter(EventService.fw_to_police == 1).all()


def get_active_fire_service_event() -> List[str]:
    return EventService.query.filter(EventService.fw_to_fire_service == 1).all()


def set_event_as_archived(event_id: int) -> NoReturn:
    event = Event.query.filter(Event.id == event_id)
    if event:
        event.archived = 1
        DB.session.commit()
