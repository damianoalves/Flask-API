import query
import sqlite3
from flask_restful import Resource, reqparse
from models.user import User


class UserRegister(Resource):

    # this parser will going to require username and password for any user that will be created
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This argument cannot be blank.")
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This argument cannot be blank."
                        )

    # post method used to create a new user
    @staticmethod
    def post():
        connection = sqlite3.connect('api.db')
        cursor = connection.cursor()
        data = UserRegister.parser.parse_args()
        if User.find_by_username(data['username']) is None:
            cursor.execute(query.insert_user, (data['username'], data['password']))
        else:
            return {"message": "User " + data['username'] + " already exists, please choose another username!"}, 400
        connection.commit()
        connection.close()
        return {"message": "User " + data['username'] + " created!"}, 201
