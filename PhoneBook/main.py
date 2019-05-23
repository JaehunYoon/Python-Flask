from flask import Flask, render_template, request, jsonify

import json

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/phone")
def phonebook():
    user = request.args.get("user")
    phone = request.args.get("phone")
    return jsonify({"user": user, "phone": phone})


if __name__ == "__main__":
    app.run("127.0.0.1", 8765, debug=True)
