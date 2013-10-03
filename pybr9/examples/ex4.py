from flask import Flask
from flask.views import MethodView
app = Flask(__name__)

class GetMixin(object):
    def get(self):
        return "Hello World, with GET, " \
               "from a mixin!"

class HelloView(MethodView, GetMixin):
    def post(self):
        return "Hello World, with POST, " \
               "from a class-based view!"

app.add_url_rule('/',
    view_func=HelloView.as_view("hello"),
    methods=["GET", "POST"])
