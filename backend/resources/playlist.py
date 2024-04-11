from flask_restful import Resource, reqparse, fields, marshal
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import abort

from backend.models import Playlist, User, db


class PlaylistResource(Resource):
    def get(self):
        pass

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass


class PlaylistsResource(Resource):

    album_fields = {
        "id": fields.Integer,
        "title": fields.String,
    }

    artist_fields = {
        "id": fields.Integer,
        "name": fields.String,
    }

    song_fields = {
        "id": fields.Integer,
        "title": fields.String,
        "genre": fields.String,
        "album": fields.nested(album_fields),
        "artist": fields.nested(artist_fields),
    }

    playlist_fields = {
        "id": fields.Integer,
        "title": fields.String,
        "user_id": fields.Integer,
        "songs": fields.List(fields.Nested(song_fields)),
    }

    @jwt_required()
    def get(self, user_id):
        if user_id != get_jwt_identity():
            abort(403, "You are not authorized to view this profile")
        user = User.query.get(user_id)
        if not user:
            abort(404, "User ID: {} doesn't exist".format(user_id))
        if user.playlists:
            playlists = [
                marshal(playlist, self.playlist_fields) for playlist in user.playlists
            ]
            return playlists, 200
        else:
            print("No playlists found")
            return {"message": "No playlists found"}, 404
