from flask import Flask, abort, jsonify
app = Flask(__name__)

@app.errorhandler(412)
def handler(error):
    return jsonify(status_code=error.code,
                   description=error.description)

@app.route("/")
def hello():
    abort(412)

