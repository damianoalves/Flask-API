# import libraries
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.users import UserRegister
from resources.item import Item, ItemList
import create_table

# flask, api and JWT inicialized with some config
app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///api.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.secret_key = "damiano"
jwt = JWT(app, authenticate, identity)


# created db tables before the first request
@app.before_first_request
def create_tables():
    db.create_all()


# routes
api.add_resource(ItemList, '/items')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(UserRegister, '/singup')

if __name__ == '__main__':
    from db import db

    db.init_app(app)
    app.run(port=1337, debug=True)
