import uuid
from datetime import datetime

from _app import db


class FormOnasilingTongkangStsModel(db.Model):
    __tablename__ = 'form_onasiling_tongkang_sts'
    id = db.Column(db.String, primary_key=True, default=lambda: uuid.uuid4().hex)
    tr_shipment_status_id = db.Column(db.String)
    arrival_at_anchorage = db.Column(db.DateTime)
    tender_at_vessel = db.Column(db.DateTime)
    commance_loading_disch = db.Column(db.DateTime)
    completed_loading_disch = db.Column(db.DateTime)
    total_loading_mt = db.Column(db.Integer)
    loading_area = db.Column(db.String)
    add_by = db.Column(db.String)
    add_time = db.Column(db.DateTime, default=lambda: datetime.now())
    ket = db.Column(db.String)

    def __init__(self, tr_shipment_status_id, arrival_at_anchorage, tender_at_vessel, commance_loading_disch, completed_loading_disch, total_loading_mt, loading_area, add_by, ket):
        self.tr_shipment_status_id = tr_shipment_status_id
        self.arrival_at_anchorage = arrival_at_anchorage
        self.tender_at_vessel = tender_at_vessel
        self.commance_loading_disch = commance_loading_disch
        self.completed_loading_disch = completed_loading_disch
        self.total_loading_mt = total_loading_mt
        self.loading_area = loading_area
        self.add_by = add_by
        self.ket = ket

    def json(self):
        return {
            'id': self.id,
            'tr_shipment_status_id': self.tr_shipment_status_id,
            'arrival_at_anchorage': self.arrival_at_anchorage,
            'tender_at_vessel': self.tender_at_vessel,
            'commance_loading_disch': self.commance_loading_disch,
            'completed_loading_disch': self.completed_loading_disch,
            'total_loading_mt': self.total_loading_mt,
            'loading_area': self.loading_area,
            'add_by': self.add_by,
            'add_time': self.add_time,
            'ket': self.ket,
        }
