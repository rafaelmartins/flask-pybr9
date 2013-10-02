from flask import Flask, Blueprint
bp = Blueprint("views", __name__)

@bp.route("/")
def hello():
    return "Hello World from a blueprint, with an app factory!"

def create_app():
    app = Flask(__name__)
    app.register_blueprint(bp, url_prefix="/")
    return app

if __name__ == "__main__":
    create_app().run()
