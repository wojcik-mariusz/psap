from . import DB

from sqlalchemy.orm import relationship


# dir should be named 'Models'

class Event(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    event_date = DB.Column(DB.DateTime, nullable=False)
    description = DB.Column(DB.String)
    archived = DB.Column(DB.Boolean)
    event_address = relationship("EventAddress", backref="event")
    event_service = relationship("EventService", backref="event")
    event_reporter = relationship("EventReporter", backref="event")


class EventAddress(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    voivodeship = DB.Column(DB.String, nullable=False)
    district = DB.Column(DB.String, nullable=False)
    community = DB.Column(DB.String, nullable=False)
    town = DB.Column(DB.String, nullable=False)
    street = DB.Column(DB.String)
    street_number = DB.Column(DB.Integer, nullable=False)
    event_id = DB.Column(DB.ForeignKey("event.id"))

class EventService(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    fw_to_police = DB.Column(DB.Boolean)
    fw_to_paramedic = DB.Column(DB.Boolean)
    fw_to_fire_service = DB.Column(DB.Boolean)
    event_id = DB.Column(DB.ForeignKey("event.id"))

class EventReporter(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    caller_name = DB.Column(DB.String)
    caller_telephone_number = DB.Column(DB.Integer, nullable=False)
    caller_surname = DB.Column(DB.String)
    event_id = DB.Column(DB.ForeignKey("event.id"))

