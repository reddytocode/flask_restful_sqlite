from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username', required=True, help="This field can not be blank.")
    parser.add_argument('password', required=True, help="This field can not be blank.")

    def post(self):
        data = UserRegister.parser.parse_args()

        username = data['username']

        if UserModel.find_by_username(username):
            return {"message": "User exists."}, 400

        user = UserModel(**data)
        user.save_to_db()

        return {"message": "User created successfully"}, 201
