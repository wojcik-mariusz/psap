from . import DB

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
#
#
# class EventService(DB.Model):
#     id = DB.Column(DB.Integer, primary_key=True)
#     event_id = DB.Column(DB.Integer, )
#     fw_to_police = DB.Column(DB.Boolean)
#     fw_to_paramedic = DB.Column(DB.Boolean)
#     fw_to_fire_service = DB.Column(DB.Boolean)
#
#
# class EventReporter(DB.Model):
#     caller_name = DB.Column(DB.String)
#     caller_telephone_number = DB.Column(DB.Integer, nullable=False)
#     caller_surname = DB.Column(DB.String)
#
#
# class EventPlace(DB.Model):
#     town = DB.Column(DB.String, nullable=False)
#     street = DB.Column(DB.String)
#     street_number = DB.Column(DB.Integer, nullable=False)
#     voivodeship = DB.Column(DB.String, nullable=False)
#     district = DB.Column(DB.String, nullable=False)
#     community = DB.Column(DB.String, nullable=False)
