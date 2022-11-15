from datetime import datetime

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

main_v = Blueprint("main_v", __name__, template_folder="templates")


@main_v.route("/index")
@main_v.route("/dashboard")
@main_v.route("/")
def dashboard():
    try:
        tgl = datetime.now()
        return render_template("index.html", bulan=tgl.strftime("%b"))
    except TemplateNotFound:
        abort(404)


@main_v.route("/data_chart")
def data_chart():
    return {"data_ship": [15, 1, 9, 2, 6, 8, 4, 3, 3, 1, 0, 0],
            "data_cargo": [275590659 / 1000, 212933143 / 1000, 240744035 / 1000, 223580065 / 1000, 226774140 / 1000,
                           187555053 / 1000, 130272911 / 1000, 0, 0, 0, 2, 0]}


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


@main_v.route("/long-towing")
def longtowing():
    try:
        return render_template("long_towing.html")
    except TemplateNotFound:
        abort(404)


@main_v.route("/m-vessel-sts")
def mvesselsts():
    try:
        return render_template("m_vessel_sts.html")
    except TemplateNotFound:
        abort(404)


@main_v.route("/barge-sts")
def bargests():
    try:
        return render_template("barge_sts.html")
    except TemplateNotFound:
        abort(404)


@main_v.route("/barge-long-towing")
def bargelongtowing():
    try:
        return render_template("barge_long_towing.html")
    except TemplateNotFound:
        abort(404)


@main_v.route("/report")
def report():
    try:
        return render_template("report.html")
    except TemplateNotFound:
        abort(404)
