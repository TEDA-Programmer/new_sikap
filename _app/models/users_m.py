import uuid

from flask_login import UserMixin
from sqlalchemy import or_
from werkzeug.security import check_password_hash

from _app import db, login_manager


@login_manager.user_loader
def load_user(account_id):
    return UsersModel.query.get(account_id)


class UsersModel(db.Model, UserMixin):
    __tablename__ = 'users'

    # region Column
    id = db.Column(db.String, primary_key=True, default=lambda: uuid.uuid4().hex)
    auth_id = db.Column(db.Integer)
    username = db.Column(db.String)
    hashed_password = db.Column(db.String)
    nama = db.Column(db.String)
    email = db.Column(db.String)
    grup = db.Column(db.String)
    area = db.Column(db.String)
    opr = db.Column(db.String)
    cabang = db.Column(db.String)
    delete_status = db.Column(db.Integer, default=0)

    # endregion

    def __init__(self, auth_id, username, hashed_password, nama, email, grup, area, opr, cabang, delete_status):
        self.auth_id = auth_id
        self.username = username
        self.hashed_password = hashed_password
        self.nama = nama
        self.email = email
        self.grup = grup
        self.area = area
        self.opr = opr
        self.cabang = cabang
        self.delete_status = delete_status

    def json(self):
        return {
            'id': self.id,
            'auth_id': self.auth_id,
            'username': self.username,
            'nama': self.nama,
            'email': self.email,
            'grup': self.grup,
            'area': self.area,
            'opr': self.opr,
            'cabang': self.cabang,
            'delete_status': self.delete_status,
        }

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)

    @classmethod
    def by_username(cls, username):
        return cls.query.filter(or_(cls.username == username, cls.email == username)).first()
