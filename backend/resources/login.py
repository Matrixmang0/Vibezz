from backend.models import User, db
from flask_restful import Resource, reqparse, abort
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from datetime import timedelta

cred_parser = reqparse.RequestParser()
cred_parser.add_argument("username", type=str, required=True)
cred_parser.add_argument("password", type=str, required=True)


class LoginResource(Resource):
    def post(self):
        args = cred_parser.parse_args()
        user = User.query.filter_by(username=args["username"]).first()
        if not user:
            print(f'User {args["username"]} does not exist')
            abort(404, message=f'User {args["username"]} does not exist')
        if not user.check_password(args["password"]):
            print("Invalid password")
            abort(403, message="Invalid password")
        access_token = create_access_token(
            identity=user.id, expires_delta=timedelta(hours=1)
        )
        return {"access_token": access_token}, 200

    @jwt_required()
    def get(self):
        user = User.query.get(get_jwt_identity())
        return {
            "login": True,
            "message": "Logged in as {}".format(user.username),
        }, 200
