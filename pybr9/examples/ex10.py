from flask import Flask
from werkzeug.exceptions import PreconditionFailed
app = Flask(__name__)

class MyPreconditionFailed(PreconditionFailed):
    description = 'Ooops... the precondition failed! :P'

@app.route("/")
def hello():
    raise MyPreconditionFailed

