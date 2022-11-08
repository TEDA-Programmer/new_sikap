import uuid
from datetime import datetime

from _app import db


class ShipmentModel(db.Model):
    __tablename__ = 'shipment'
    id = db.Column(db.String, primary_key=True, default=lambda: uuid.uuid4().hex)
    capt_kapal = db.Column(db.String)
    shipper_id = db.Column(db.String)
    agen_id = db.Column(db.String)
    bl_number = db.Column(db.String)
    muatan_cargo_bl = db.Column(db.Integer)
    pelabuhan_muat = db.Column(db.String)
    ket = db.Column(db.String)

    def __init__(self, capt_kapal, shipper_id, agen_id, bl_number, muatan_cargo_bl, pelabuhan_muat, ket):
        self.capt_kapal = capt_kapal
        self.shipper_id = shipper_id
        self.agen_id = agen_id
        self.bl_number = bl_number
        self.muatan_cargo_bl = muatan_cargo_bl
        self.pelabuhan_muat = pelabuhan_muat
        self.ket = ket

    def json(self):
        return {
            'id': self.id,
            'capt_kapal': self.capt_kapal,
            'shipper_id': self.shipper_id,
            'agen_id': self.agen_id,
            'bl_number': self.bl_number,
            'muatan_cargo_bl': self.muatan_cargo_bl,
            'pelabuhan_muat': self.pelabuhan_muat,
            'ket': self.ket,
        }
