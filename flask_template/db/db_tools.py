from . import DB


class Events(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    voivodeship = DB.Column(DB.String(30), nullable=False)
    district = DB.Column(DB.String(100), nullable=False)
    community = DB.Column(DB.String(50), nullable=False)
    town = DB.Column(DB.String(50), nullable=False)


