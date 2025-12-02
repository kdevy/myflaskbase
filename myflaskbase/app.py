from flask import Flask
from .models import User
from .config import DevConfig
from .extensions import login_manager
from .extensions import db

def create_app(config_object=DevConfig):
    app = Flask(__name__)
    app.config.from_object(config_object)

    # Init extensions
    db.init_app(app)
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    with app.app_context():
        db.create_all()

    login_manager.login_view = "user.login"

    from .blueprints.user import user_bp
    app.register_blueprint(user_bp)

    return app