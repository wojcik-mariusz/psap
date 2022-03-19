from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    from flask_template.server import SERVER_BLUEPRINT
    app.register_blueprint(SERVER_BLUEPRINT)

    return app
