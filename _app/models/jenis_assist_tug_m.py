import uuid
from datetime import datetime

from _app import db


class JenisAssistTugModel(db.Model):
    __tablename__ = 'jenis_assist_tug'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    jenis_name = db.Column(db.String)
    ket = db.Column(db.String)

    def __init__(self, jenis_name, ket):
        self.jenis_name = jenis_name
        self.ket = ket

    def json(self):
        return {
            'id': self.id,
            'jenis_name': self.jenis_name,
            'ket': self.ket,
        }
