from flask import Blueprint
from flask_login import login_required
from .views.login_view import LoginView
from .views.register_view import RegisterView
from .views.logout_view import LogoutView
from .views.home_view import HomeView

user_bp = Blueprint("user", __name__, template_folder="templates")

login_view = LoginView.as_view("login")
user_bp.add_url_rule("/login" \
                    , view_func=login_view \
                    , methods=["GET", "POST"])

register_view = RegisterView.as_view("register")
user_bp.add_url_rule("/register" \
                    , view_func=register_view \
                    , methods=["GET", "POST"])

logout_view = LogoutView.as_view("logout")
logout_view = login_required(logout_view)
user_bp.add_url_rule("/logout" \
                    , view_func=logout_view \
                    , methods=["GET"])

home_view = HomeView.as_view("home")
home_view = login_required(home_view)
user_bp.add_url_rule("/home" \
                    , view_func=home_view \
                    , methods=["GET"])