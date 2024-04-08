from flask_restful import Resource, reqparse, fields, marshal_with, marshal
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import abort
from backend.models import Album, User, db


post_parser = reqparse.RequestParser()
post_parser.add_argument("title", type=str, required=True)
post_parser.add_argument("description", type=str, required=True)


class AlbumResource(Resource):
    def get(self):
        pass

    @jwt_required()
    def post(self, user_id):
        if user_id != get_jwt_identity():
            abort(403, "You are not authorized to view this page")
        user = User.query.get(user_id)
        if not user:
            abort(404, "User ID: {} doesn't exist".format(user_id))

        args = post_parser.parse_args()

        title = args["title"]
        description = args["description"]

        if title == "" or description == "":
            abort(404, "Please fill all the fields")

        album = Album(
            title=args["title"],
            description=args["description"],
            artist_id=user_id,
        )

        user.role_id = "art"

        db.session.add(album)
        db.session.commit()

        return ({"message": "Album created successfully"}, 201)

    def put(self):
        pass

    def delete(self):
        pass


class AlbumsResource(Resource):

    album_fields = {
        "id": fields.Integer,
        "title": fields.String,
        "description": fields.String,
    }

    @jwt_required()
    def get(self, user_id):
        if user_id != get_jwt_identity():
            abort(403, "You are not authorized to view this profile")
        user = User.query.get(user_id)
        if not user:
            abort(404, "User ID: {} doesn't exist".format(user_id))
        if user.created_albums:
            albums = [
                marshal(album, self.album_fields) for album in user.created_albums
            ]
            return albums, 200
        else:
            print("No albums found")
            return ({"msg": "No albums found"}, 200)

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass
