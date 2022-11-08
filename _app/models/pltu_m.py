import uuid

from _app import db


class PltuModel(db.Model):
    __tablename__ = 'pltu'
    id = db.Column(db.String, primary_key=True, default=lambda: uuid.uuid4().hex)
    pltu_name = db.Column(db.String)
    capacity = db.Column(db.Integer)
    area = db.Column(db.String)
    cabang = db.Column(db.String)
    kode = db.Column(db.String)
    regional = db.Column(db.String)
    delete_status = db.Column(db.Integer, default=0)

    def __init__(self, pltu_name, capacity, area, cabang, kode, regional, delete_status):
        self.pltu_name = pltu_name
        self.capacity = capacity
        self.area = area
        self.cabang = cabang
        self.kode = kode
        self.regional = regional
        self.delete_status = delete_status

    def json(self):
        return {
            'id': self.id,
            'pltu_name': self.pltu_name,
            'capacity': self.capacity,
            'area': self.area,
            'cabang': self.cabang,
            'kode': self.kode,
            'regional': self.regional,
            'delete_status': self.delete_status,
        }
