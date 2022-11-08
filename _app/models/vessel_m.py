import uuid
from datetime import datetime

from _app import db


class VesselModel(db.Model):
    __tablename__ = 'vessel'
    id = db.Column(db.String, primary_key=True, default=lambda: uuid.uuid4().hex)
    nama_vessel = db.Column(db.String)
    pemilik_vessel = db.Column(db.String)
    bendera = db.Column(db.String)
    kelas = db.Column(db.String)
    tahun = db.Column(db.Integer)
    grt = db.Column(db.Integer)
    dwt = db.Column(db.Integer)
    nrt = db.Column(db.Integer)
    loa = db.Column(db.Integer)
    sarat_muka = db.Column(db.String)
    sarat_belakang = db.Column(db.String)
    ket = db.Column(db.String)
    add_by = db.Column(db.String)
    add_time = db.Column(db.DateTime, default=lambda: datetime.now())

    def __init__(self, nama_vessel, pemilik_vessel, bendera, kelas, tahun, grt, dwt, nrt, loa, sarat_muka, sarat_belakang, ket, add_by):
        self.nama_vessel = nama_vessel
        self.pemilik_vessel = pemilik_vessel
        self.bendera = bendera
        self.kelas = kelas
        self.tahun = tahun
        self.grt = grt
        self.dwt = dwt
        self.nrt = nrt
        self.loa = loa
        self.sarat_muka = sarat_muka
        self.sarat_belakang = sarat_belakang
        self.ket = ket
        self.add_by = add_by

    def json(self):
        return {
            'id': self.id,
            'nama_vessel': self.nama_vessel,
            'pemilik_vessel': self.pemilik_vessel,
            'bendera': self.bendera,
            'kelas': self.kelas,
            'tahun': self.tahun,
            'grt': self.grt,
            'dwt': self.dwt,
            'nrt': self.nrt,
            'loa': self.loa,
            'sarat_muka': self.sarat_muka,
            'sarat_belakang': self.sarat_belakang,
            'ket': self.ket,
            'add_by': self.add_by,
            'add_time': self.add_time,
        }
