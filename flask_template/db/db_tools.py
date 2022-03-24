from . import DB


class Events(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    event_date = DB.Column(DB.DateTime, nullable=False)
    voivodeship = DB.Column(DB.String, nullable=False)
    district = DB.Column(DB.String, nullable=False)
    community = DB.Column(DB.String, nullable=False)
    town = DB.Column(DB.String, nullable=False)
    street = DB.Column(DB.String)
    street_number = DB.Column(DB.Integer, nullable=False)
    fw_to_police = DB.Column(DB.Boolean)
    fw_to_paramedic = DB.Column(DB.Boolean)
    fw_to_fire_service = DB.Column(DB.Boolean)
    caller_telephone_number = DB.Column(DB.Integer, nullable=False)
    caller_name = DB.Column(DB.String)
    caller_surname = DB.Column(DB.String)


