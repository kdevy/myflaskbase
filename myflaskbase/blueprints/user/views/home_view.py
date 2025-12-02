from flask import render_template
from flask.views import MethodView

class HomeView(MethodView):
    def get(self):
        context = {}
        return render_template("home.html", **context)
