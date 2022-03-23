from . import DB


class Events(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    event_date = DB.Column(DB.DateTime)
    voivodeship = DB.Column(DB.String(30), nullable=False)
    district = DB.Column(DB.String(100), nullable=False)
    community = DB.Column(DB.String(50), nullable=False)
    town = DB.Column(DB.String(50), nullable=False)
    street = DB.Column(DB.String(50))
    street_number = DB.Column(DB.Integer(10), nullable=False)
    fw_to_police = DB.Column(DB.Bollean)
    fw_to_paramedic = DB.Column(DB.Bollean)
    fw_to_fire_service = DB.Column(DB.Bollean)
    caller_telephone_number = DB.Column(DB.Integer(15), nullable=False)
    caller_name = DB.Column(DB.String)
    caller_surname = DB.Model(DB.String)


