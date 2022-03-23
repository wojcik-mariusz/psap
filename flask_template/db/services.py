from typing import NoReturn
from datetime import datetime

from db_tools import Events
from . import DB

def insert_new_event(
        voivodeship: str,
        district: int,
        community: str,
        town: str,
        street: str,
        street_number: int,
        fw_to_police: bool,
        fw_to_paramedic: bool,
        fw_to_fire_service: bool,
        caller_telephone_number: int,
        caller_name: str,
        caller_surname: str
) -> NoReturn:
    event = Events(
        event_date=datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
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
