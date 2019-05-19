import socket

from flask import *

app = Flask(__name__)


@app.route("/")
def main():
    return "<h1>h4lo~~</h1>"


@app.route("/red")
def red():
    return redirect(url_for('hello'))


@app.route("/hello")
def hello():
    return render_template("hello.html")


@app.route("/input")
def input():
    return render_template("input_exam.html")


@app.route("/input/<example>")
def input_value(example):
    return render_template("input_exam.html", **{'example': example})


if __name__ == "__main__":
    # app.run("127.0.0.1", 8787, debug=True)
    # auto get hostname
    app.run(socket.gethostbyname(socket.gethostname()), 8230, debug=False)
    # 배포 시에는 debug를 False로 해두자
