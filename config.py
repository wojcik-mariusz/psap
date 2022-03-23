from dataclasses import dataclass
from string import ascii_letters
from random import sample


@dataclass
class Config:
    SECRET_KEY = "".join(sample(ascii_letters, 10))
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
    SQLALCHEMY_DATABASE_URI = "sqlite3:///db/event_db.db"
    DEBUG = True
