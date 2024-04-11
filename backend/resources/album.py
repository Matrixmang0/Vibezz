from flask_restful import Resource, reqparse, fields, marshal_with, marshal
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import abort
from backend.models import Album, User, db


post_parser = reqparse.RequestParser()
post_parser.add_argument("title", type=str, required=True)
post_parser.add_argument("description", type=str, required=True)


class AlbumResource(Resource):

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


class EditAlbumResource(Resource):

    @jwt_required()
    def put(self, user_id, album_id):
        if user_id != get_jwt_identity():
            abort(403, message="You are not authorized to view this page")
        user = User.query.get(user_id)
        if not user:
            abort(404, message="User ID: {} doesn't exist".format(user_id))
        album = Album.query.filter_by(id=album_id).first()
        if not album:
            abort(404, message="No album found")
        args = post_parser.parse_args()
        album.title = args["title"]
        album.description = args["description"]
        db.session.commit()
        return {"message": "Album updated successfully"}, 200


class AlbumName(Resource):

    album_fields = {
        "id": fields.Integer,
        "title": fields.String,
        "description": fields.String,
    }

    @jwt_required()
    @marshal_with(album_fields)
    def get(self, user_id, album_id):
        if user_id != get_jwt_identity():
            abort(403, "You are not authorized to view this page")
        user = User.query.get(user_id)
        if not user:
            abort(404, "User ID: {} doesn't exist".format(user_id))
        album = Album.query.filter_by(id=album_id).first()
        if not album:
            abort(404, "Album ID: {} doesn't exist".format(album_id))
        return album, 200


class DeleteAlbumResource(Resource):

    @jwt_required()
    def delete(self, user_id, album_id):
        try:
            if user_id != get_jwt_identity():
                abort(403, message="You are not authorized to view this page")

            user = User.query.get(user_id)
            if not user:
                abort(404, message="User ID: {} doesn't exist".format(user_id))

            album = Album.query.filter_by(id=album_id).first()
            if not album:
                abort(404, message="No album found")

            db.session.delete(album)
            db.session.commit()

            return {"message": "Album deleted successfully"}, 200
        except Exception as e:
            abort(500, message=str(e))


class AlbumsResource(Resource):

    album_fields = {
        "id": fields.Integer,
        "title": fields.String,
        "description": fields.String,
        "songs": fields.List(fields.String),
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


class LibraryResource(Resource):

    artist_fields = {
        "id": fields.Integer,
        "name": fields.String,
    }

    song_fields = {
        "id": fields.Integer,
        "title": fields.String,
    }

    album_fields = {
        "id": fields.Integer,
        "title": fields.String,
        "artist": fields.Nested(artist_fields),
        "description": fields.String,
        "songs": fields.List(fields.Nested(song_fields)),
    }

    def get(self):

        albums = Album.query.all()
        if albums:
            albums = [marshal(album, self.album_fields) for album in albums]
            return albums, 200
        else:
            print("No albums found")
            return ({"msg": "No albums found"}, 200)
