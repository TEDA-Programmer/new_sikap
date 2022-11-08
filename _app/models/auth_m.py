from _app import db


class AuthModel(db.Model):
    __tablename__ = 'auth'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    auth_name = db.Column(db.String)

    def __init__(self, auth_name):
        self.auth_name = auth_name

    def json(self):
        return {
            'id': self.id,
            'auth_name': self.auth_name,
        }
