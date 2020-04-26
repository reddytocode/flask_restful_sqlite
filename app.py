from flask import Flask
from flask_restful import Api
from db import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

app.secret_key = 'reddy_secret_key'
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()

# Add Endpoints to API
from resources.users import UserRegister

api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)
