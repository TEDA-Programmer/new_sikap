import uuid
from datetime import datetime

from _app import db


class TrShipmentStatusModel(db.Model):
    __tablename__ = 'tr_shipment_status'
    id = db.Column(db.String, primary_key=True, default=lambda: uuid.uuid4().hex)
    shipment_id = db.Column(db.String)
    status_id = db.Column(db.Integer)
    add_by = db.Column(db.String)
    add_time = db.Column(db.String, default=lambda: datetime.now())
    pltu_tujuan_deviasi = db.Column(db.Integer)

    def __init__(self, shipment_id, status_id, add_by, pltu_tujuan_deviasi):
        self.shipment_id = shipment_id
        self.status_id = status_id
        self.add_by = add_by
        self.pltu_tujuan_deviasi = pltu_tujuan_deviasi

    def json(self):
        return {
            'id': self.id,
            'shipment_id': self.shipment_id,
            'status_id': self.status_id,
            'add_by': self.add_by,
            'add_time': self.add_time,
            'pltu_tujuan_deviasi': self.pltu_tujuan_deviasi,
        }
