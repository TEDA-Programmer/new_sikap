import uuid
from datetime import datetime

from _app import db


class AgenModel(db.Model):
    __tablename__ = "agen"

    # region Column
    id = db.Column(db.String, primary_key=True, default=lambda: uuid.uuid4().hex)
    nama_agen = db.Column(db.String)
    alamat_agen = db.Column(db.String)
    telepon_agen = db.Column(db.String)
    fax_agen = db.Column(db.String)
    email_agen = db.Column(db.String)
    pic_agen = db.Column(db.String)
    ket = db.Column(db.String)
    add_by = db.Column(db.String)
    add_time = db.Column(db.DateTime, default=lambda: datetime.now())

    # endregion

    def __init__(self, nama_agen, alamat_agen, telepon_agen, fax_agen, email_agen, pic_agen, ket, add_by):
        self.nama_agen = nama_agen
        self.alamat_agen = alamat_agen
        self.telepon_agen = telepon_agen
        self.fax_agen = fax_agen
        self.email_agen = email_agen
        self.pic_agen = pic_agen
        self.ket = ket
        self.add_by = add_by

    def json(self):
        return {
            "id": self.id,
            "nama_agen": self.nama_agen,
            "alamat_agen": self.alamat_agen,
            "telepon_agen": self.telepon_agen,
            "fax_agen": self.fax_agen,
            "email_agen": self.email_agen,
            "pic_agen": self.pic_agen,
            "ket": self.ket,
            "add_by": self.add_by,
            "add_time": self.add_time,
        }
