from flask import Flask, abort
from werkzeug.exceptions import PreconditionFailed
app = Flask(__name__)

@app.route("/")
def hello():
    raise PreconditionFailed

