import unittest
from flask import Flask, Blueprint, current_app
bp = Blueprint("views", __name__)

@bp.route("/")
def hello():
    return "Hello %s" % current_app.config["NAME"]

def create_app():
    app = Flask(__name__)
    app.register_blueprint(bp, url_prefix="/")
    return app

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config["NAME"] = 'foo'

    def test_foo(self):
        rv = self.app.test_client().get('/')
        self.assertIn("Hello foo", rv.data)

if __name__ == "__main__":
    unittest.main()
