'''Flask config'''

from flask_wtf import FlaskForm
from wtforms import widgets
from wtforms.fields import StringField, SelectField, IntegerField, SelectMultipleField, SubmitField
from wtforms.validators import data_required, length


class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


class NewEvent(FlaskForm):
    new_event_voivodeship = SelectField("Select voivodeship:", choices=[
        "dolnośląskie", "kujawsko-pomorskie", "lubelskie", "lubuskie", "łódzkie", "małopolskie", "mazowieckie",
        "opolskie", "podkarpackie", "podlaskie", "pomorskie", "śląskie", "świętokrzyskie", "warmińsko-mazurskie",
        "wielkopolskie", "zachodniopomorskie"
    ])
    new_event_district = StringField("District:", validators=[data_required()])
    new_event_community = StringField("Community:" ,validators=[data_required()])
    new_event_town = StringField("Town:", validators=[data_required()])
    new_event_street = StringField("Street:")
    new_event_street_number = IntegerField("Number:", validators=[data_required()])
    new_event_description = StringField("Event description", validators=[data_required()])
    new_event_type_of_emergency_services_needed = MultiCheckboxField('Forward event to:',
                                                                     coerce=int,
                                                                     choices=[(1, "Straż Pożarna"), (2, "Policja"), (3, "Ratownictwo medyczne")])
    new_event_caller_telephone_number = IntegerField("Telephone number:", validators=[data_required()])
    new_event_caller_name = StringField("Caller name:")
    new_event_caller_surname = StringField("Caller surname:")
    new_event_confirm_button = SubmitField("Apply event")
