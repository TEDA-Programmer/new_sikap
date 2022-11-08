import uuid
from datetime import datetime

from _app import db


class FormOnasilingModel(db.Model):
    __tablename__ = 'form_onasiling'
    id = db.Column(db.String, primary_key=True, default=lambda: uuid.uuid4().hex)
    tr_shipment_status_id = db.Column(db.String)
    time_departure = db.Column(db.DATE)
    eta_anchorage = db.Column(db.DATE)
    add_by = db.Column(db.String)
    add_time = db.Column(db.DateTime, default=lambda: datetime.now())
    ket = db.Column(db.String)

    def __init__(self, tr_shipment_status_id, time_departure, eta_anchorage, add_by, ket):
        self.tr_shipment_status_id = tr_shipment_status_id
        self.time_departure = time_departure
        self.eta_anchorage = eta_anchorage
        self.add_by = add_by
        self.ket = ket

    def json(self):
        return {
            'id': self.id,
            'tr_shipment_status_id': self.tr_shipment_status_id,
            'time_departure': self.time_departure,
            'eta_anchorage': self.eta_anchorage,
            'add_by': self.add_by,
            'add_time': self.add_time,
            'ket': self.ket,
        }
