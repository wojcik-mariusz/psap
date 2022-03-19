from flask import Blueprint

SERVER_BLUEPRINT = Blueprint("server_blueprint", __name__)

from . import routes