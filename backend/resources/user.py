from flask_restful import Resource, reqparse, fields, marshal_with, marshal
from backend.models import User, db
from email_validator import validate_email, EmailUndeliverableError
import re
from flask import abort
from flask_jwt_extended import jwt_required, get_jwt_identity

get_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "username": fields.String,
    "email": fields.String,
    "role_id": fields.String,
    "profile_img": fields.String,
}

post_parser = reqparse.RequestParser()
post_parser.add_argument("username", type=str, required=True)
post_parser.add_argument("password", type=str, required=True)
post_parser.add_argument("email", type=str, required=True)
post_parser.add_argument("name", type=str, required=True)
post_parser.add_argument("confirm_password", type=str, required=True)


put_parser = reqparse.RequestParser()
put_parser.add_argument("username", type=str, required=True)
put_parser.add_argument("name", type=str, required=True)
put_parser.add_argument("email", type=str, required=True)

pass_parser = reqparse.RequestParser()
pass_parser.add_argument("currentPassword", type=str, required=True)
pass_parser.add_argument("newPassword", type=str, required=True)
pass_parser.add_argument("reNewPassword", type=str, required=True)


class UserResource(Resource):

    @jwt_required()
    @marshal_with(get_fields)
    def get(self, user_id):
        if user_id != get_jwt_identity():
            abort(403, "You are not authorized to view this profile")
        user = User.query.get(user_id)
        if not user:
            abort(404, "User ID: {} doesn't exist".format(user_id))
        return user, 200

    @jwt_required()
    def put(self, user_id):
        if user_id != get_jwt_identity():
            abort(403, "You are not authorized to make changes to this profile")
        user = User.query.get(user_id)
        if not user:
            abort(404, "User ID: {} doesn't exist".format(user_id))

        args = put_parser.parse_args()

        name = args["name"]
        username = args["username"]
        email = args["email"]

        if not username or not email or not name:
            print("Please fill all the fields")
            abort(404, "Please fill all the fields")

        try:
            if not validate_email(email):
                print("Please enter a valid email address")
                abort(404, "Please enter a valid email address")
        except EmailUndeliverableError:
            print("The email domain does not exist")
            abort(404, "The email domain does not exist")

        user.name = name
        user.username = username
        user.email = email
        db.session.commit()
        return {"message": "Profile updated successfully"}, 200


class UsersResource(Resource):

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


class PassResource(Resource):

    @jwt_required()
    def put(self, user_id):
        if user_id != get_jwt_identity():
            abort(403, "You are not authorized to make changes to this profile")
        user = User.query.get(user_id)
        if not user:
            abort(404, "User ID: {} doesn't exist".format(user_id))

        args = pass_parser.parse_args()

        current_password = args["currentPassword"]
        new_password = args["newPassword"]
        re_new_password = args["reNewPassword"]

        if not current_password or not new_password or not re_new_password:
            print("Please fill all the fields")
            abort(404, "Please fill all the fields")

        if not user.check_password(current_password):
            print("Incorrect password")
            abort(404, "Incorrect password")
        if new_password != re_new_password:
            print("Passwords do not match")
            abort(404, "Passwords do not match")

        if len(new_password) < 8:
            print("New password should be at least 8 characters long")
            abort(404, "New password should be at least 8 characters long")
        if not re.search(r"[A-Z]", new_password):
            print("New Password should contain at least one uppercase letter")
            abort(404, "New Password should contain at least one uppercase letter")
        if not re.search(r"[a-z]", new_password):
            print("New Password should contain at least one lowercase letter")
            abort(404, "New Password should contain at least one lowercase letter")
        if not re.search(r"\d", new_password):
            print("New Password should contain at least one digit")
            abort(404, "New Password should contain at least one digit")

        user.set_password(new_password)
        db.session.commit()
        return {"message": "Password updated successfully"}, 200


class AdminUserResource(Resource):

    user_fields = {
        "id": fields.Integer,
        "name": fields.String,
        "username": fields.String,
        "email": fields.String,
        "role_id": fields.String,
    }

    @jwt_required()
    def get(self):
        if get_jwt_identity() == "0":
            abort(403, "You are not authorized to access this information")

        users = User.query.filter(User.id != 0).all()
        users = [marshal(user, self.user_fields) for user in users]
        return users, 200
