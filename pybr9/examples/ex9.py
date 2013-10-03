from flask import Flask
from werkzeug.exceptions import PreconditionFailed
app = Flask(__name__)

@app.route("/")
def hello():
    raise PreconditionFailed

