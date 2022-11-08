import uuid
from datetime import datetime

from _app import db


class ShipmentStatusModel(db.Model):
    __tablename__ = 'shipment_status'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    status_name = db.Column(db.String)
    key = db.Column(db.String)

    def __init__(self, status_name, key):
        self.status_name = status_name
        self.key = key

    def json(self):
        return {
            'id': self.id,
            'status_name': self.status_name,
            'key': self.key,
        }
