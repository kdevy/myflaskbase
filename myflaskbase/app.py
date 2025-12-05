from flask import request
from myflaskbase.extensions import login_manager, db, babel

def init_app(app, locale_selector=None):
    # Init extensions
    db.init_app(app)
    login_manager.init_app(app)
    if not locale_selector:
        def locale_selector():
            return request.accept_languages.best_match(app.config.get("LANGUAGES", ["ja", "en"]))

    babel.init_app(app, locale_selector=locale_selector)

    with app.app_context():
        db.create_all()

