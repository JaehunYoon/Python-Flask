from flask import Flask, jsonify

app = Flask(__name__)

data = {'Hello': 'Admin'}


@app.route('/')
def hello():
    return jsonify(data)


if __name__ == '__main__':
    app.run('127.0.0.1', 8765)
