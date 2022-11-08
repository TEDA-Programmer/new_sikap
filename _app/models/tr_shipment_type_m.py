import uuid
from datetime import datetime

from _app import db


class TrShipmentTypeModel(db.Model):
    __tablename__ = 'tr_shipment_type'
    id = db.Column(db.String, primary_key=True, default=lambda: uuid.uuid4().hex)
    shipment_id = db.Column(db.String)
    type_id = db.Column(db.Integer)
    tugboat_id = db.Column(db.String)
    tongkang_id = db.Column(db.String)
    vessel_id = db.Column(db.String)
    spb_id = db.Column(db.String)
    shipment_sts_id = db.Column(db.String)

    def __init__(self, shipment_id, type_id, tugboat_id, tongkang_id, vessel_id, spb_id, shipment_sts_id):
        self.shipment_id = shipment_id
        self.type_id = type_id
        self.tugboat_id = tugboat_id
        self.tongkang_id = tongkang_id
        self.vessel_id = vessel_id
        self.spb_id = spb_id
        self.shipment_sts_id = shipment_sts_id

    def json(self):
        return {
            'id': self.id,
            'shipment_id': self.shipment_id,
            'type_id': self.type_id,
            'tugboat_id': self.tugboat_id,
            'tongkang_id': self.tongkang_id,
            'vessel_id': self.vessel_id,
            'spb_id': self.spb_id,
            'shipment_sts_id': self.shipment_sts_id,
        }
