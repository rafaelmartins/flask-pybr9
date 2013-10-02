from flask import Flask, Blueprint
app = Flask(__name__)
bp = Blueprint("views", __name__)

@bp.route("/")
def hello():
    return "Hello World from a blueprint!"

app.register_blueprint(bp, url_prefix="/")
