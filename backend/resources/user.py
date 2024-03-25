from flask_restful import Resource, reqparse, fields, marshal_with
from backend.models import User, db
from email_validator import validate_email, EmailUndeliverableError
import re
from flask import abort, jsonify

get_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "username": fields.String,
    "email": fields.String,
    "role_id": fields.String,
}

post_parser = reqparse.RequestParser()
post_parser.add_argument("username", type=str, required=True)
post_parser.add_argument("password", type=str, required=True)
post_parser.add_argument("email", type=str, required=True)
post_parser.add_argument("name", type=str, required=True)
post_parser.add_argument("confirm_password", type=str, required=True)


class UserResource(Resource):

    @marshal_with(get_fields)
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
        args = post_parser.parse_args()

        name = args["name"]
        username = args["username"]
        email = args["email"]
        password = args["password"]
        confirm_password = args["confirm_password"]

        if (
            not username
            or not password
            or not confirm_password
            or not email
            or not name
        ):
            print("Please fill all the fields")
            abort(404, "Please fill all the fields")

        if password != confirm_password:
            print("Passwords do not match")
            abort(404, "Passwords do not match")

        try:
            if not validate_email(email):
                print("Please enter a valid email address")
                abort(404, "Please enter a valid email address")
        except EmailUndeliverableError:
            print("The email domain does not exist")
            abort(404, "The email domain does not exist")

        user = User.query.filter_by(email=email).first()

        if user:
            print("Email already exists")
            abort(404, "Email already exists")

        if len(password) < 8:
            print("Password should be at least 8 characters long")
            abort(404, "Password should be at least 8 characters long")

        if not re.search(r"[A-Z]", password):
            print("Password should contain at least one uppercase letter")
            abort(404, "Password should contain at least one uppercase letter")

        if not re.search(r"[a-z]", password):
            print("Password should contain at least one lowercase letter")
            abort(404, "Password should contain at least one lowercase letter")

        if not re.search(r"\d", password):
            print("Password should contain at least one digit")
            abort(404, "Password should contain at least one digit")

        user = User.query.filter_by(username=username).first()

        if user:
            print(f"Username {username} already exists")
            abort(404, f"Username {username} already exists")

        new_user = User(
            username=username,
            email=email,
            name=name,
        )

        new_user.set_password(password)

        db.session.add(new_user)
        db.session.commit()
        return {"message": "User created successfully"}, 201
