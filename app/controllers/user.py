from flask_restful import Resource, reqparse


class User(Resource):
    def get(self, id):
        pass

    def put(self, id):
        pass

    def patch(self, todo_id):
        pass

    def delete(self, todo_id):
        pass

class UserList(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('nickname',
                        type=str,
                        required=True,
                        help="This argument cannot be blank.")
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This argument cannot be blank."
                        )

    def get(self):
        pass

    def post(self):
        pass


