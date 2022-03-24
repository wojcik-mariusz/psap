from flask import render_template, request

from . import SERVER_BLUEPRINT
from flask_template.server.forms import NewEvent
from flask_template.db.services import insert_new_event


@SERVER_BLUEPRINT.route("/")
def home():
    form = NewEvent()
    return render_template("index.html", form=form)


@SERVER_BLUEPRINT.route("/add-new-event", methods=['GET', 'POST'])
def add_new_event():
    form = NewEvent()
    if request.method == 'POST':
        insert_new_event(
            voivodeship=form.new_event_voivodeship.data,
            district=form.new_event_district.data,
            community=form.new_event_community.data,
            town=form.new_event_town.data,
            street=form.new_event_street.data,
            street_number=form.new_event_street_number.data,
            list_of_emergency_services_needed=form.new_event_type_of_emergency_services_needed.data,
            caller_telephone_number=form.new_event_caller_telephone_number.data,
            caller_name=form.new_event_caller_name.data,
            caller_surname=form.new_event_caller_surname.data
        )
    return render_template("add-new-event.html", form=form)
