from flask_login import login_user
from werkzeug.security import generate_password_hash, check_password_hash
from myflaskbase.extensions import db
from myflaskbase.blueprints.user.models import User

class UserService:
    @staticmethod
    def login(username, password):
        user = User.query.filter_by(username=username).first()
        if not user or not check_password_hash(user.password, password):
            raise ValueError("Invalid credentials")
        login_user(user)
        return {"username": username}

    @staticmethod
    def register(data):
        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            raise ValueError("Username and password are required")

        user = User.query.filter_by(username=username).first()

        if user:
            raise ValueError("User already exists")

        user = User(username=username, password=generate_password_hash(password))
        db.session.add(user)
        db.session.commit()
        return {"username": username}
