from flask_restful import Resource, reqparse, fields, marshal_with
from backend.models import User, db
from flask import abort

parser = reqparse.RequestParser()
parser.add_argument("name", type=str, required=True, help="This field cannot be blank")
parser.add_argument(
    "username", type=str, required=True, help="This field cannot be blank"
)
parser.add_argument("email", type=str, required=True, help="This field cannot be blank")
parser.add_argument(
    "password", type=str, required=True, help="This field cannot be blank"
)
parser.add_argument(
    "profile_img", type=str, required=True, help="This field cannot be blank"
)
parser.add_argument(
    "role_id", type=str, required=True, help="This field cannot be blank"
)

user_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "username": fields.String,
    "email": fields.String,
    "role_id": fields.String,
}


class UserResource(Resource):
    @marshal_with(user_fields)
    def get(self, user_id):
        user = User.query.get(user_id)
        if not user:
            abort(404, {"error": "User ID: {} doesn't exist".format(user_id)})
        return user, 200

    def put(self):
        pass

    def delete(self):
        pass


class UsersResource(Resource):
    def get(self):
        pass

    def post(self):
        pass
