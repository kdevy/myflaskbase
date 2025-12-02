from myflaskbase.blueprints.user.models import User
from myflaskbase.extensions import login_manager
from myflaskbase.extensions import db

def init_app(app):
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