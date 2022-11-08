import uuid
from datetime import datetime

from _app import db


class ShipperModel(db.Model):
    __tablename__ = 'shipper'
    id = db.Column(db.String, primary_key=True, default=lambda: uuid.uuid4().hex)
    nama_shipper = db.Column(db.String)
    alamat_shipper = db.Column(db.String)
    telepon_shipper = db.Column(db.String)
    fax_shipper = db.Column(db.String)
    email_shipper = db.Column(db.String)
    pic_shipper = db.Column(db.String)
    ket = db.Column(db.String)
    add_by = db.Column(db.String)
    add_time = db.Column(db.DateTime, default=lambda: datetime.now())

    def __init__(self, nama_shipper, alamat_shipper, telepon_shipper, fax_shipper, email_shipper, pic_shipper, ket, add_by):
        self.nama_shipper = nama_shipper
        self.alamat_shipper = alamat_shipper
        self.telepon_shipper = telepon_shipper
        self.fax_shipper = fax_shipper
        self.email_shipper = email_shipper
        self.pic_shipper = pic_shipper
        self.ket = ket
        self.add_by = add_by

    def json(self):
        return {
            'id': self.id,
            'nama_shipper': self.nama_shipper,
            'alamat_shipper': self.alamat_shipper,
            'telepon_shipper': self.telepon_shipper,
            'fax_shipper': self.fax_shipper,
            'email_shipper': self.email_shipper,
            'pic_shipper': self.pic_shipper,
            'ket': self.ket,
            'add_by': self.add_by,
            'add_time': self.add_time,
        }
