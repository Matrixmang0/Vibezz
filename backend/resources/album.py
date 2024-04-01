from flask_restful import Resource, reqparse, fields, marshal_with
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import abort
from backend.models import Album, User


class AlbumResource(Resource):
    def get(self):
        pass

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass


class AlbumsResource(Resource):

    @jwt_required()
    def get(self, user_id):
        if user_id != get_jwt_identity():
            abort(403, "You are not authorized to view this profile")
        user = User.query.get(user_id)
        if not user:
            abort(404, "User ID: {} doesn't exist".format(user_id))
        if user.created_albums:
            return user.created_albums, 200
        else:
            return {"msg": "No albums found"}, 200

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass
