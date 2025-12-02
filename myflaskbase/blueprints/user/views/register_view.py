from flask import jsonify, render_template
from flask.views import MethodView
from myflaskbase.blueprints.user.services import UserService
from myflaskbase.blueprints.user.forms import RegisterForm

class RegisterView(MethodView):
    form = None

    def dispatch_request(self, *args, **kwargs):
        self.form = RegisterForm()
        return super().dispatch_request(*args, **kwargs)

    def get(self):
        context = {"form": self.form}
        return render_template("register.html", **context)

    def post(self):
        data = None
        try:
            if self.form.validate_on_submit():
                data = self.form.data
            else:
                raise ValueError("Invalid form submission")

            new_user = UserService.register(data)
            return jsonify({"message": "Registered", "user": new_user}), 201
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
