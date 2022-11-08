import uuid
from datetime import datetime

from _app import db


class ShipmentTypeModel(db.Model):
    __tablename__ = 'shipment_type'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type_name = db.Column(db.String)
    ket = db.Column(db.String)

    def __init__(self, type_name, ket):
        self.type_name = type_name
        self.ket = ket

    def json(self):
        return {
            'id': self.id,
            'type_name': self.type_name,
            'ket': self.ket,
        }
