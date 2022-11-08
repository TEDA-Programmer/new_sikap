import uuid
from datetime import datetime

from _app import db


class FormCastOfJettyModel(db.Model):
    __tablename__ = 'form_cast_of_jetty'
    id = db.Column(db.String, primary_key=True, default=lambda: uuid.uuid4().hex)
    tr_shipment_status_id = db.Column(db.String)
    cast_of_jetty = db.Column(db.DateTime)
    commence_completed = db.Column(db.DateTime)
    final_draught_survey = db.Column(db.NUMERIC)
    add_by = db.Column(db.String)
    add_time = db.Column(db.DateTime, default=lambda: datetime.now())
    ket = db.Column(db.String)

    def __init__(self, tr_shipment_status_id, cast_of_jetty, commence_completed, final_draught_survey, add_by, ket):
        self.tr_shipment_status_id = tr_shipment_status_id
        self.cast_of_jetty = cast_of_jetty
        self.commence_completed = commence_completed
        self.final_draught_survey = final_draught_survey
        self.add_by = add_by
        self.ket = ket

    def json(self):
        return {
            'id': self.id,
            'tr_shipment_status_id': self.tr_shipment_status_id,
            'cast_of_jetty': self.cast_of_jetty,
            'commence_completed': self.commence_completed,
            'final_draught_survey': self.final_draught_survey,
            'add_by': self.add_by,
            'add_time': self.add_time,
            'ket': self.ket,
        }
