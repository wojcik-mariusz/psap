from . import DB

from sqlalchemy.orm import relationship


# dir should be named 'Models'


class Events(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    event_date = DB.Column(DB.DateTime, nullable=False)
    voivodeship = DB.Column(DB.String, nullable=False)
    district = DB.Column(DB.String, nullable=False)
    community = DB.Column(DB.String, nullable=False)
    town = DB.Column(DB.String, nullable=False)
    street = DB.Column(DB.String)
    street_number = DB.Column(DB.Integer, nullable=False)
    description = DB.Column(DB.String)
    fw_to_police = DB.Column(DB.Boolean, nullable=False, default=False)
    fw_to_paramedic = DB.Column(DB.Boolean, nullable=False, default=False)
    fw_to_fire_service = DB.Column(DB.Boolean, nullable=False, default=False)
    caller_telephone_number = DB.Column(DB.Integer, nullable=False)
    caller_name = DB.Column(DB.String)
    caller_surname = DB.Column(DB.String)
    archived = DB.Column(DB.Boolean, default=False)


# class Event(DB.Model):
#     id = DB.Column(DB.Integer, primary_key=True)
#     event_date = DB.Column(DB.DateTime, nullable=False)
#     description = DB.Column(DB.String)
#     archived = DB.Column(DB.Boolean)
#     even_service = relationship("EventService", back_populates="event")
#     event_reporter = relationship("EventReporter", back_populates="event", uselist=False)
#
#
# class EventService(DB.Model):
#     id = DB.Column(DB.Integer, primary_key=True)
#     fw_to_police = DB.Column(DB.Boolean)
#     fw_to_paramedic = DB.Column(DB.Boolean)
#     fw_to_fire_service = DB.Column(DB.Boolean)
#     event_id = DB.Column(DB.Interger, DB.ForeignKey('event.id'))
#
#
# class EventReporter(DB.Model):
#     caller_name = DB.Column(DB.String)
#     caller_telephone_number = DB.Column(DB.Integer, nullable=False)
#     caller_surname = DB.Column(DB.String)
#     event = relationship("Event", back_populates="eventreporter")

#
#

#
#

#
#
# class EventPlace(DB.Model):
#     town = DB.Column(DB.String, nullable=False)
#     street = DB.Column(DB.String)
#     street_number = DB.Column(DB.Integer, nullable=False)
#     voivodeship = DB.Column(DB.String, nullable=False)
#     district = DB.Column(DB.String, nullable=False)
#     community = DB.Column(DB.String, nullable=False)
