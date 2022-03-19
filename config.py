from dataclasses import dataclass
from string import ascii_letters
from random import sample

@dataclass
class Config:
    SECRET_KEY = "".join(sample(ascii_letters, 10))
    DEBUG = True