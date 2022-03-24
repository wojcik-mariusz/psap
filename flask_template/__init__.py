from flask import Flask

from flask_template.db import DB


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    from flask_template.server import SERVER_BLUEPRINT
    app.register_blueprint(SERVER_BLUEPRINT)

    DB.init_app(app)
    with app.app_context():
        DB.create_all()

    return app
