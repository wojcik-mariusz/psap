from flask import render_template
from . import SERVER_BLUEPRINT

@SERVER_BLUEPRINT.route("/")
def home():
    return render_template("index.html")