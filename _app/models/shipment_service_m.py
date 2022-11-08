import uuid
from datetime import datetime

from _app import db


class ShipmentServiceModel(db.Model):
    __tablename__ = 'shipment_service'
    id = db.Column(db.String, primary_key=True, default=lambda: uuid.uuid4().hex)
    shipment_id = db.Column(db.String)
    agent = db.Column(db.Integer, default=0)
    assist_tug = db.Column(db.Integer, default=0)
    sts = db.Column(db.Integer, default=0)
    jetty_management = db.Column(db.Integer, default=0)
    pbm = db.Column(db.Integer, default=0)
    add_by = db.Column(db.String)
    add_time = db.Column(db.DateTime, default=lambda: datetime.now())

    def __init__(self, shipment_id, agent, assist_tug, sts, jetty_management, pbm, add_by):
        self.shipment_id = shipment_id
        self.agent = agent
        self.assist_tug = assist_tug
        self.sts = sts
        self.jetty_management = jetty_management
        self.pbm = pbm
        self.add_by = add_by

    def json(self):
        return {
            'id': self.id,
            'shipment_id': self.shipment_id,
            'agent': self.agent,
            'assist_tug': self.assist_tug,
            'sts': self.sts,
            'jetty_management': self.jetty_management,
            'pbm': self.pbm,
            'add_by': self.add_by,
            'add_time': self.add_time,
        }
