from flask import Flask, request
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello():
    if request.method == "GET":
        return "Hello World, with GET!"
    if request.method == "POST":
        return "Hello World, with POST!"
