import datetime

from flask import render_template, make_response, request, flash
from typing import List

from . import SERVER_BLUEPRINT, ERROR_HANDLER_BLUEPRINT
from flask_template.server.forms import NewEvent
from flask_template.db import DB
from flask_template.server.services.event_manager import get_all_list_event, get_active_paramedic_list_event, \
    get_active_police_list_event, get_active_fire_service_event
from flask_template.db.db_tools import Event, EventService, EventReporter, EventAddress


# TODO errors
@SERVER_BLUEPRINT.route("/")
def home():
    form = NewEvent()
    return render_template("index.html", form=form)


@SERVER_BLUEPRINT.route("/add-new-event", methods=['GET', 'POST'])
def add_new_event():
    form = NewEvent()
    if request.method == "POST":
        event = Event(
            event_date=datetime.datetime.now().replace(microsecond=0),
            description=form.new_event_description.data
        )
        address = EventAddress(
            voivodeship=form.new_event_voivodeship.data,
            district=form.new_event_district.data,
            community=form.new_event_community.data,
            town=form.new_event_town.data,
            street=form.new_event_street.data,
            street_number=form.new_event_street_number.data
        )
        service = EventService(
            fw_to_police=form.new_event_fw_to_police.data,
            fw_to_paramedic=form.new_event_fw_to_paramedic.data,
            fw_to_fire_service=form.new_event_fw_to_fire_service.data
        )
        reporter = EventReporter(
            caller_telephone_number=form.new_event_caller_telephone_number.data,
            caller_name=form.new_event_caller_name.data,
            caller_surname=form.new_event_caller_surname.data
        )
        event.event_address.append(address)
        event.event_service.append(service)
        event.event_reporter.append(reporter)
        DB.session.add_all([event, address, service, reporter])
        DB.session.commit()
        flash("Event added succesfully.")

    return render_template("add-new-event.html", form=form)


@SERVER_BLUEPRINT.route('/paramedic-all')
def show_paramedic_events():
    paramedic_events: List[str] = get_active_paramedic_list_event()
    return render_template('paramedic-show-all.html', paramedic_events=paramedic_events)


@SERVER_BLUEPRINT.route('/police-all')
def show_police_active_events():
    police_active_events_list = get_active_police_list_event()
    return render_template("police-show-all.html", police_events=police_active_events_list)


@SERVER_BLUEPRINT.route('/fire-all')
def show_fire_service_active_events():
    fire_service_active_events_list = get_active_fire_service_event()
    return render_template("fire-show-all.html", fire_service_events=fire_service_active_events_list)


@SERVER_BLUEPRINT.route('/active-events')
def show_active_events():
    active_events = get_all_list_event()
    return render_template('active-events.html', active_events=active_events)


@ERROR_HANDLER_BLUEPRINT.errorhandler(404)
def page_not_found(_):
    '''Page not found'''
    return make_response(render_template("404.html", title="404", content="Page not found"), 404)
