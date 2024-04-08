from flask_restful import Resource, reqparse, fields, marshal_with, marshal
from flask_jwt_extended import jwt_required, get_jwt_identity

from backend.models import User, Album
import datetime
from flask import abort


class SongResource(Resource):
    def get(self):
        pass

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass


class SongsResource(Resource):

    song_fields = {
        "id": fields.Integer,
        "title": fields.String,
        "lyrics": fields.String,
        "genre": fields.String,
    }

    @marshal_with(song_fields)
    @jwt_required()
    def get(self, album_id, user_id):

        if user_id != get_jwt_identity():
            abort(403, "You are not authorized to view this profile")

        user = User.query.get(user_id)
        if not user:
            abort(404, "User ID: {} doesn't exist".format(user_id))

        album = Album.query.get(album_id)
        if not album:
            abort(404, "Album ID: {} doesn't exist".format(album_id))

        if album.songs:
            songs = [marshal(song, self.song_fields) for song in album.songs]
            return songs, 200
        else:
            print("No songs found")
            return ({"msg": "No songs found"}, 200)

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass
