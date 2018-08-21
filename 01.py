from flask import Flask

app = Flask(__name__)

@app.route('/')

def index():
    return "h4lo"

@app.route('/custom/<int:param>')

def custom(param):
    return param

if __name__ == '__main__':
    app.run()