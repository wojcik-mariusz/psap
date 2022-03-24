from typing import NoReturn, List
from datetime import datetime

from flask_template.db.db_tools import Events
from . import DB


def insert_new_event(
        voivodeship: str,
        district: int,
        community: str,
        town: str,
        street: str,
        street_number: int,
        list_of_emergency_services_needed: List[str],
        caller_telephone_number: int,
        caller_name: str,
        caller_surname: str
) -> NoReturn:
    fw_to_fire_service = True if 1 in list_of_emergency_services_needed else False
    fw_to_police = True if 2 in list_of_emergency_services_needed else False
    fw_to_paramedic = True if 3 in list_of_emergency_services_needed else False
    event = Events(
        event_date=datetime.now(),
        voivodeship=voivodeship,
        district=district,
        community=community,
        town=town,
        street=street,
        street_number=street_number,
        fw_to_police=fw_to_police,
        fw_to_paramedic=fw_to_paramedic,
        fw_to_fire_service=fw_to_fire_service,
        caller_telephone_number=caller_telephone_number,
        caller_name=caller_name,
        caller_surname=caller_surname
    )
    DB.session.add(event)
    DB.session.commit()
