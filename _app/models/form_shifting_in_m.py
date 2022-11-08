import uuid
from datetime import datetime

from _app import db


class FormShiftingInModel(db.Model):
    __tablename__ = 'form_shifting_in'
    id = db.Column(db.String, primary_key=True, default=lambda: uuid.uuid4().hex)
    tr_shipment_status_id = db.Column(db.String)
    time_shifting_in = db.Column(db.DateTime)
    add_by = db.Column(db.String)
    add_time = db.Column(db.DateTime, default=lambda: datetime.now())
    ket = db.Column(db.String)

    def __init__(self, tr_shipment_status_id, time_shifting_in, add_by, ket):
        self.tr_shipment_status_id = tr_shipment_status_id
        self.time_shifting_in = time_shifting_in
        self.add_by = add_by
        self.ket = ket

    def json(self):
        return {
            'id': self.id,
            'tr_shipment_status_id': self.tr_shipment_status_id,
            'time_shifting_in': self.time_shifting_in,
            'add_by': self.add_by,
            'add_time': self.add_time,
            'ket': self.ket,
        }
