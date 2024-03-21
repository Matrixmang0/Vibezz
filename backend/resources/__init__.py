from flask_restful import Api
from app import app
from flask_jwt_extended import JWTManager

jwt = JWTManager(app)

api = Api(app, prefix="/api")

from backend.resources.user import UserResource
from backend.resources.login import LoginResource

api.add_resource(LoginResource, "/login")
api.add_resource(UserResource, "/user/<int:user_id>")
