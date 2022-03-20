from flask import render_template
from . import SERVER_BLUEPRINT
from flask_template.server.forms import NewEvent


@SERVER_BLUEPRINT.route("/")
def home():
    form = NewEvent()
    return render_template("index.html", form=form)


@SERVER_BLUEPRINT.route("/add-new-event")
def add_new_event():
    form = NewEvent()
    return render_template("add-new-event.html", form=form)
