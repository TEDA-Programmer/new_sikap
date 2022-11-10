from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

main_v = Blueprint("main_v", __name__, template_folder="templates")


@main_v.route("/index")
@main_v.route("/dashboard")
@main_v.route("/")
def dashboard():
    try:
        return render_template("index.html")
    except TemplateNotFound:
        abort(404)


@main_v.route("/shipment")
def shipment():
    try:
        return render_template("shipment.html")
    except TemplateNotFound:
        abort(404)


@main_v.route("/my-shipment")
def myshipment():
    try:
        return render_template("my_shipment.html")
    except TemplateNotFound:
        abort(404)


@main_v.route("/line-up")
def lineup():
    try:
        return render_template("line_up.html")
    except TemplateNotFound:
        abort(404)
