import uuid
from datetime import datetime

from _app import db


class ShipmentDocsModel(db.Model):
    __tablename__ = 'shipment_docs'
    id = db.Column(db.String, primary_key=True, default=lambda: uuid.uuid4().hex)
    shipment_id = db.Column(db.String)
    doc_filename = db.Column(db.String)
    add_by = db.Column(db.String)
    add_time = db.Column(db.String, default=lambda: datetime.now())
    shipment_status = db.Column(db.String)
    ket = db.Column(db.String)

    def __init__(self, shipment_id, doc_filename, add_by, shipment_status, ket):
        self.shipment_id = shipment_id
        self.doc_filename = doc_filename
        self.add_by = add_by
        self.shipment_status = shipment_status
        self.ket = ket

    def json(self):
        return {
            'id': self.id,
            'shipment_id': self.shipment_id,
            'doc_filename': self.doc_filename,
            'add_by': self.add_by,
            'add_time': self.add_time,
            'shipment_status': self.shipment_status,
            'ket': self.ket,
        }
