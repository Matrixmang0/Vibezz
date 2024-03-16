from flask_restful import Api
from app import app

api = Api(app, prefix="/api")

from backend.resources.user import UserResource

api.add_resource(UserResource, "/user/<int:user_id>")
