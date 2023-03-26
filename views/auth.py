from flask import Blueprint, render_template, redirect, url_for, request
from logic.common_main import get_data
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from models.users import User
from forms.register_user_form import RegisterUserForm
from models.init_db import db
from sqlalchemy.exc import IntegrityError, DataError
from logs import my_loger

auth_app = Blueprint('auth_app', __name__)

login_manager = LoginManager()
login_manager.login_view = 'auth_app.login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).one_or_none()


@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for("auth_app.login"))


@auth_app.route("/login/", methods=["GET", "POST"], endpoint="login")
def login():
    if request.method == "GET":
        return render_template("auth/login.html")
    username = request.form.get("username")
    if not username:
        return render_template("auth/login.html", error="username not passed")
    user = User.query.filter_by(username=username).one_or_none()
    if user is None:
        return render_template("auth/login.html", error=f"no user {username!r} found")
    login_user(user)
    return redirect(url_for("index"))


@auth_app.route("/logout/", endpoint="logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))


@auth_app.route("/secret/")
@login_required
def secret_view():
    return "Super secret data"


@auth_app.route("/register_user/", methods=["POST", "GET"], endpoint='register_user')
def register_user():
    if current_user.is_authenticated:
        return redirect('/auth/user_detail.html')
    else:
        form = RegisterUserForm(request.form)

        if request.method == "POST" and form.validate_on_submit():
            error = None
            user = User()
            user.email = form.email.data
            user.first_name = form.first_name.data
            user.last_name = form.last_name.data
            user.username = form.username.data

            try:
                db.session.add(user)
                db.session.commit()
            except IntegrityError or DataError as error:
                my_loger.error(f'Неудалось создать пользователя auth.py {error}')
                return render_template('/auth/register.html', form=form, error=error)

            login_user(user)
            return render_template('/auth/user_detail.html', form=form, error=error)

        return render_template('/auth/register.html', form=form)


@auth_app.route("/user_details/", endpoint='user_details')
@login_required
def user_details():
    return render_template('auth/user_detail.html')


__all__ = [
    "login_manager",
    "auth_app",
]
