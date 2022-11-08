import uuid
from datetime import datetime

from _app import db


class FormShiftingOutModel(db.Model):
    __tablename__ = 'form_shifting_out'
    id = db.Column(db.String, primary_key=True, default=lambda: uuid.uuid4().hex)
    tr_shipment_status_id = db.Column(db.String)
    time_shifting_out = db.Column(db.DateTime)
    add_by = db.Column(db.String)
    add_time = db.Column(db.DateTime, default=lambda: datetime.now())
    ket = db.Column(db.String)

    def __init__(self, tr_shipment_status_id, time_shifting_out, add_by, ket):
        self.tr_shipment_status_id = tr_shipment_status_id
        self.time_shifting_out = time_shifting_out
        self.add_by = add_by
        self.ket = ket

    def json(self):
        return {
            'id': self.id,
            'tr_shipment_status_id': self.tr_shipment_status_id,
            'time_shifting_out': self.time_shifting_out,
            'add_by': self.add_by,
            'add_time': self.add_time,
            'ket': self.ket,
        }
