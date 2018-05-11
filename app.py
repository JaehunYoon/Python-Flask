# -*- coding: utf-8 -*-

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
    return "<h1>h4lo~~</h1>"

@app.route("/hello")
def hello():
    return render_template("hello.html")

if __name__ == "__main__":
    app.run(port=8080, debug=True)