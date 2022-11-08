import uuid
from datetime import datetime

from _app import db


class FormAnchorageModel(db.Model):
    __tablename__ = 'form_anchorage'
    id = db.Column(db.String, primary_key=True, default=lambda: uuid.uuid4().hex)
    tr_shipment_status_id = db.Column(db.String)
    time_arrival_anchorage = db.Column(db.DateTime)
    eta_berthed = db.Column(db.DATE)
    est_complete_sts = db.Column(db.DATE)
    balance_unloading_sts = db.Column(db.Integer)
    add_by = db.Column(db.String)
    add_time = db.Column(db.DateTime, default=lambda: datetime.now())
    ket = db.Column(db.String)

    def __init__(self, tr_shipment_status_id, time_arrival_anchorage, eta_berthed, est_complete_sts, balance_unloading_sts, add_by, ket):
        self.tr_shipment_status_id = tr_shipment_status_id
        self.time_arrival_anchorage = time_arrival_anchorage
        self.eta_berthed = eta_berthed
        self.est_complete_sts = est_complete_sts
        self.balance_unloading_sts = balance_unloading_sts
        self.add_by = add_by
        self.ket = ket

    def json(self):
        return {
            'id': self.id,
            'tr_shipment_status_id': self.tr_shipment_status_id,
            'time_arrival_anchorage': self.time_arrival_anchorage,
            'eta_berthed': self.eta_berthed,
            'est_complete_sts': self.est_complete_sts,
            'balance_unloading_sts': self.balance_unloading_sts,
            'add_by': self.add_by,
            'add_time': self.add_time,
            'ket': self.ket,
        }
