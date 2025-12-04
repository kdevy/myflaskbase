from flask import request
from myflaskbase.blueprints.user.models import User
from myflaskbase.extensions import login_manager, db, babel

def init_app(app, locale_selector=None):
    # Init extensions
    db.init_app(app)
    login_manager.init_app(app)
    if not locale_selector:
        def locale_selector():
            return request.accept_languages.best_match(app.config.get("LANGUAGES", ["ja", "en"]))

    babel.init_app(app, locale_selector=locale_selector)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    with app.app_context():
        db.create_all()

    login_manager.login_view = "user.login"

    from .blueprints.user import user_bp
    app.register_blueprint(user_bp)