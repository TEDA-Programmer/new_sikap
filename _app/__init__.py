import os

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/new_sikap'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.urandom(24)

db = SQLAlchemy(app)

# region Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'account_v.login'

# endregion

from _app.views.user import user_v
from _app.views.main import main_v

app.register_blueprint(user_v)
app.register_blueprint(main_v)


@app.route('/')
def hello_world():
    return 'Hello World!'
