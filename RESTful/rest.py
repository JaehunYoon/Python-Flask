from flask import *
from flask_restful import *

app = Flask(__name__, template_folder="../templates")
api = Api(app)  # get api object


@app.route('/')
def index():
    return render_template('register.html')


class LoginExample(Resource):
    def post(self):
        new_username = request.form['username']
        new_password = request.form['password']

        if new_username == 'h4lo' and new_password == 'passwd':
            return f'Hello {new_username}', 200
        else:
            return 204

api.add_resource(LoginExample, '/auth')

if __name__ == '__main__':
    app.run('127.0.0.1', 8765, debug=True)
