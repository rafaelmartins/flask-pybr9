from flask import Flask, abort
app = Flask(__name__)

@app.route("/")
def hello():
    abort(412)

