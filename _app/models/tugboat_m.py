import uuid
from datetime import datetime

from _app import db


class TugboatModel(db.Model):
    __tablename__ = 'tugboat'
    id = db.Column(db.String, primary_key=True, default=lambda: uuid.uuid4().hex)
    nama_tugboat = db.Column(db.String)
    pemilik_tugboat = db.Column(db.String)
    ket = db.Column(db.String)
    add_by = db.Column(db.String)
    add_time = db.Column(db.DateTime, default=lambda: datetime.now())

    def __init__(self, nama_tugboat, pemilik_tugboat, ket, add_by):
        self.nama_tugboat = nama_tugboat
        self.pemilik_tugboat = pemilik_tugboat
        self.ket = ket
        self.add_by = add_by

    def json(self):
        return {
            'id': self.id,
            'nama_tugboat': self.nama_tugboat,
            'pemilik_tugboat': self.pemilik_tugboat,
            'ket': self.ket,
            'add_by': self.add_by,
            'add_time': self.add_time,
        }
