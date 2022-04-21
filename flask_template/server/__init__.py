from flask import Blueprint

SERVER_BLUEPRINT = Blueprint("server_blueprint", __name__)
ERROR_HANDLER_BLUEPRINT = Blueprint("error_handler", __name__)

from . import routes