import uuid
from datetime import datetime

from _app import db


class AssistTugModel(db.Model):
    __tablename__ = 'assist_tug'
    id = db.Column(db.String, primary_key=True, default=lambda: uuid.uuid4().hex)
    shipment_id = db.Column(db.String)
    jenis_assist_id = db.Column(db.Integer)
    nama_tugboat1 = db.Column(db.String)
    master_tugboat1 = db.Column(db.String)
    start_time1 = db.Column(db.DateTime)
    end_time1 = db.Column(db.DateTime)
    nama_tugboat2 = db.Column(db.String)
    master_tugboat2 = db.Column(db.String)
    start_time2 = db.Column(db.DateTime)
    end_time2 = db.Column(db.DateTime)
    nama_pandu = db.Column(db.String)
    naik_time = db.Column(db.DateTime)
    turun_time = db.Column(db.DateTime)
    add_by = db.Column(db.String)
    add_time = db.Column(db.DateTime, default=lambda: datetime.now())
    nama_debitur = db.Column(db.String)
    alamat = db.Column(db.String)
    biaya_politage = db.Column(db.Integer)
    total = db.Column(db.Integer)

    def __init__(self, shipment_id, jenis_assist_id, nama_tugboat1, master_tugboat1, start_time1, end_time1, nama_tugboat2, master_tugboat2, start_time2, end_time2, nama_pandu, naik_time, turun_time, add_by, nama_debitur, alamat, biaya_politage, total):
        self.shipment_id = shipment_id
        self.jenis_assist_id = jenis_assist_id
        self.nama_tugboat1 = nama_tugboat1
        self.master_tugboat1 = master_tugboat1
        self.start_time1 = start_time1
        self.end_time1 = end_time1
        self.nama_tugboat2 = nama_tugboat2
        self.master_tugboat2 = master_tugboat2
        self.start_time2 = start_time2
        self.end_time2 = end_time2
        self.nama_pandu = nama_pandu
        self.naik_time = naik_time
        self.turun_time = turun_time
        self.add_by = add_by
        self.nama_debitur = nama_debitur
        self.alamat = alamat
        self.biaya_politage = biaya_politage
        self.total = total

    def json(self):
        return {
            'id': self.id,
            'shipment_id': self.shipment_id,
            'jenis_assist_id': self.jenis_assist_id,
            'nama_tugboat1': self.nama_tugboat1,
            'master_tugboat1': self.master_tugboat1,
            'start_time1': self.start_time1,
            'end_time1': self.end_time1,
            'nama_tugboat2': self.nama_tugboat2,
            'master_tugboat2': self.master_tugboat2,
            'start_time2': self.start_time2,
            'end_time2': self.end_time2,
            'nama_pandu': self.nama_pandu,
            'naik_time': self.naik_time,
            'turun_time': self.turun_time,
            'add_by': self.add_by,
            'add_time': self.add_time,
            'nama_debitur': self.nama_debitur,
            'alamat': self.alamat,
            'biaya_politage': self.biaya_politage,
            'total': self.total,
        }
