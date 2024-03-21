from flask import session, request, jsonify, make_response
from app import app
from jwt import decode, encode, DecodeError, ExpiredSignatureError
from werkzeug.exceptions import BadRequest, NotFound
from backend.models import User
from datetime import datetime, timedelta
from functools import wraps


def admin_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split(" ")[1]

        response = jsonify({"message": {"error": ""}})

        if not token:
            response["message"]["error"] = "Token is missing"
            return make_response(response, 401)

        try:
            data = decode(token, app.config["SECRET_KEY"], algorithms=["HS256"])
            current_user = User.query.filter_by(id=data["user_id"]).first()

            if not current_user:
                response["message"]["error"] = f"User {data['username']} not found"
                return make_response(response, 404)

            exp_time = datetime.strptime(data["exp"])
            current_time = datetime.now()

            if current_time > exp_time:
                response["message"]["error"] = "Token is expired"
                return make_response(response, 401)

            if current_user.role_id in ["usr", "art"]:
                response["message"]["error"] = f"User {data["username"]} cannot view this page"
                return make_response(response, 403)

            return f(current_user, *args, **kwargs)

        except NotFound:
            return jsonify({"message": {"error": "Page Not Found"}}), 404

        except DecodeError:
            return jsonify({"message": {"error": "Invalid Token"}}), 401

        except ExpiredSignatureError:
            return jsonify({"message": {"error": "Token is expired"}}), 401

        except BadRequest:
            return jsonify({"message": {"error": "Bad Request"}}), 400

    return decorated


def user_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split(" ")[1]

        response = jsonify({"message": {"error": ""}})

        if not token:
            response["message"]["error"] = "Token is missing"
            return make_response(response, 401)

        try:
            data = decode(token, app.config["SECRET_KEY"], algorithms=["HS256"])
            current_user = User.query.filter_by(id=data["user_id"]).first()

            if not current_user:
                response["message"]["error"] = f"User {data['username']} not found"
                return make_response(response, 404)

            exp_time = datetime.strptime(data["exp"])
            current_time = datetime.now()

            if current_time > exp_time:
                response["message"]["error"] = "Token is expired"
                return make_response(response, 401)

            if current_user.role_id == "adm":
                response["message"]["error"] = "Admin cannot view this page"
                return make_response(response, 403)

            return f(current_user, *args, **kwargs)

        except NotFound:
            return jsonify({"message": {"error": "Page Not Found"}}), 404

        except DecodeError:
            return jsonify({"message": {"error": "Invalid Token"}}), 401

        except ExpiredSignatureError:
            return jsonify({"message": {"error": "Token is expired"}}), 401

        except BadRequest:
            return jsonify({"message": {"error": "Bad Request"}}), 400

    return decorated


@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", "")
    password = request.json.get("password", "")
    user = User.query.filter_by(username=username).first()
    if not user:
        return (
            jsonify({"message": {"error": "User {} not found".format(username)}}),
            404,
        )

    if user.password != password:
        return jsonify({"message": {"error": "Incorrect Password"}}), 404

    jwt = encode(
        {
            "username": user.username,
            "user_id": user.id,
            "exp": datetime.now() + timedelta(minutes=30),
        },
        app.config["SECRET_KEY"],
        algorithm="HS256",
    )

    return (
        jsonify(
            {
                "token": jwt,
                "user_id": user.id,
                "username": user.username,
                "role_id": user.role_id,
                "expiring_time": datetime.now() + timedelta(minutes=30).strftime("%s"),
            }
        ),
        200,
    )
