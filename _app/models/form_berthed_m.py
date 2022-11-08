import uuid
from datetime import datetime

from _app import db


class FormBerthedModel(db.Model):
    __tablename__ = 'form_berthed'
    id = db.Column(db.String, primary_key=True, default=lambda: uuid.uuid4().hex)
    tr_shipment_status_id = db.Column(db.String)
    time_from_anchorage = db.Column(db.DateTime)
    time_berthed = db.Column(db.DateTime)
    nor_tendered = db.Column(db.DateTime)
    nor_accepted = db.Column(db.DateTime)
    commence_discharge = db.Column(db.DateTime)
    est_completed = db.Column(db.DATE)
    est_cast_of = db.Column(db.DATE)
    add_by = db.Column(db.String)
    add_time = db.Column(db.DateTime, default=lambda: datetime.now())
    ket = db.Column(db.String)

    def __init__(self, tr_shipment_status_id, time_from_anchorage, time_berthed, nor_tendered, nor_accepted, commence_discharge, est_completed, est_cast_of, add_by, ket):
        self.tr_shipment_status_id = tr_shipment_status_id
        self.time_from_anchorage = time_from_anchorage
        self.time_berthed = time_berthed
        self.nor_tendered = nor_tendered
        self.nor_accepted = nor_accepted
        self.commence_discharge = commence_discharge
        self.est_completed = est_completed
        self.est_cast_of = est_cast_of
        self.add_by = add_by
        self.ket = ket

    def json(self):
        return {
            'id': self.id,
            'tr_shipment_status_id': self.tr_shipment_status_id,
            'time_from_anchorage': self.time_from_anchorage,
            'time_berthed': self.time_berthed,
            'nor_tendered': self.nor_tendered,
            'nor_accepted': self.nor_accepted,
            'commence_discharge': self.commence_discharge,
            'est_completed': self.est_completed,
            'est_cast_of': self.est_cast_of,
            'add_by': self.add_by,
            'add_time': self.add_time,
            'ket': self.ket,
        }
