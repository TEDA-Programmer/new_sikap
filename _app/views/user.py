from flask import Blueprint, render_template, abort, url_for, redirect, request, session
from flask_login import current_user, login_user, logout_user
from jinja2 import TemplateNotFound

from _app.models.users_m import UsersModel

user_v = Blueprint("user_v", __name__, template_folder="templates")


@user_v.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        ke = url_for('main_v.dashboard') if 'next' not in request.values else request.values['next']
        return redirect(ke)

    if request.method == 'POST':
        par = request.values
        print(par)
        _account = UsersModel.by_username(par['username'])
        if _account and _account.check_password(par['password']):
            login_user(_account, remember=eval(par['remember']))
            if par['next'] != "":
                _next = par['next']
            else:
                session.pop('_flashes', None)
                _next = url_for('main_v.dashboard')
            return {"login_status": "success", "next": _next}, 200
        else:
            return {"login_status": "fail", "message": "User not found"}, 400

    try:
        return render_template("login.html")
    except TemplateNotFound:
        abort(404)


@user_v.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('user_v.login'))
