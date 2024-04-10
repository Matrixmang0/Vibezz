from flask_restful import Resource, reqparse, fields, marshal_with, marshal
from flask_jwt_extended import jwt_required, get_jwt_identity

from backend.models import User, Album, Song, db
import datetime
from flask import abort


post_parser = reqparse.RequestParser()
post_parser.add_argument("title", type=str, required=True)
post_parser.add_argument("genre", type=str, required=True)
post_parser.add_argument("album_id", type=int, required=True)
post_parser.add_argument("lyrics", type=str, required=True)


class SongResource(Resource):

    def get(self):
        pass

    @jwt_required()
    def post(self, user_id):

        if user_id != get_jwt_identity():
            abort(403, "You are not authorized to view this profile")

        user = User.query.get(user_id)

        if not user:
            abort(404, "User ID: {} doesn't exist".format(user_id))

        args = post_parser.parse_args()

        title = args["title"]
        genre = args["genre"]
        album_id = args["album_id"]
        lyrics = args["lyrics"]

        if title == "" or genre == "" or album_id == "" or lyrics == "":
            abort(404, "Please fill all the fields")

        song = Song(
            title=title,
            genre=genre,
            artist_id=user_id,
            album_id=album_id,
            lyrics=lyrics,
            date_created=datetime.datetime.now(),
        )

        db.session.add(song)
        db.session.commit()

        return ({"message": "Song created successfully"}, 201)

    def put(self):
        pass


class DeleteSongResource(Resource):

    @jwt_required()
    def delete(self, user_id, song_id):

        if user_id != get_jwt_identity():
            abort(403, "You are not authorized to view this profile")

        user = User.query.get(user_id)
        if not user:
            abort(404, "User ID: {} doesn't exist".format(user_id))

        song = Song.query.get(song_id)
        if not song:
            abort(404, "Song ID: {} doesn't exist".format(song_id))

        db.session.delete(song)
        db.session.commit()

        return ({"message": "Song deleted successfully"}, 200)


class SongsResource(Resource):

    song_fields = {
        "id": fields.Integer,
        "title": fields.String,
        "lyrics": fields.String,
        "genre": fields.String,
    }

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
