from flask_restful import Resource, reqparse, fields, marshal
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import abort, request
import datetime

from backend.models import Playlist, User, Song, playlist_song_association, db


class PlaylistResource(Resource):

    artist_fields = {
        "id": fields.Integer,
        "name": fields.String,
    }

    album_fields = {
        "id": fields.Integer,
        "title": fields.String,
    }

    songs_fields = {
        "id": fields.Integer,
        "title": fields.String,
        "genre": fields.String,
        "album": fields.Nested(album_fields),
        "artist": fields.Nested(artist_fields),
        "lyrics": fields.String,
    }

    get_playlist_fields = {
        "id": fields.Integer,
        "title": fields.String,
        "date_created": fields.DateTime,
        "songs": fields.List(fields.Nested(songs_fields)),
    }

    @jwt_required()
    def get(self, playlist_id, user_id):
        if user_id != get_jwt_identity():
            abort(403, "You are not authorized to view this page")
        user = User.query.get(user_id)
        if not user:
            abort(404, "User ID: {} doesn't exist".format(user_id))
        playlist = Playlist.query.filter_by(id=playlist_id).first()
        if not playlist:
            abort(404, "Playlist ID: {} doesn't exist".format(playlist_id))
        playlist = marshal(playlist, self.get_playlist_fields)
        return playlist, 200

    @jwt_required()
    def put(self, playlist_id, user_id):
        if user_id != get_jwt_identity():
            abort(403, "You are not authorized to view this page")
        user = User.query.get(user_id)
        if not user:
            abort(404, "User ID: {} doesn't exist".format(user_id))
        playlist = Playlist.query.filter_by(id=playlist_id).first()
        if not playlist:
            abort(404, "Playlist ID: {} doesn't exist".format(playlist_id))
        parser = reqparse.RequestParser()
        parser.add_argument("title", type=str, required=True)
        args = parser.parse_args()
        title = args["title"]
        if title == "":
            abort(404, "Please fill all the fields")
        playlist.title = title
        db.session.add(playlist)
        db.session.commit()
        return {"message": "Playlist renamed successfully"}, 201

    @jwt_required()
    def delete(self, user_id, playlist_id):
        if user_id != get_jwt_identity():
            abort(403, "You are not authorized to view this page")
        user = User.query.get(user_id)
        if not user:
            abort(404, "User ID: {} doesn't exist".format(user_id))
        playlist = Playlist.query.filter_by(id=playlist_id).first()
        if not playlist:
            abort(404, "Playlist ID: {} doesn't exist".format(playlist_id))
        db.session.delete(playlist)
        db.session.commit()
        return {"message": "Playlist deleted successfully"}, 200


class PostPlaylistResource(Resource):

    @jwt_required()
    def post(self, user_id):
        if user_id != get_jwt_identity():
            abort(403, "You are not authorized to view this page")
        user = User.query.get(user_id)
        if not user:
            abort(404, "User ID: {} doesn't exist".format(user_id))
        parser = reqparse.RequestParser()
        parser.add_argument("title", type=str, required=True)
        args = parser.parse_args()
        title = args["title"]
        if title == "":
            abort(404, "Please fill all the fields")
        date_created = datetime.datetime.now()
        playlist = Playlist(
            title=title,
            user_id=user_id,
            date_created=date_created,
        )
        db.session.add(playlist)
        db.session.commit()
        return {"message": "Playlist created successfully"}, 201


class PutPlaylistResource(Resource):

    @jwt_required()
    def put(self, user_id, playlist_id):
        if user_id != get_jwt_identity():
            abort(403, "You are not authorized to view this profile")
        user = User.query.get(user_id)
        if not user:
            abort(404, "User ID: {} doesn't exist".format(user_id))
        parser = reqparse.RequestParser()
        parser.add_argument("title", type=str, required=True)
        args = parser.parse_args()
        title = args["title"]
        if title == "":
            abort(404, "Please fill all the fields")

        playlist = Playlist.query.filter_by(id=playlist_id).first()
        if not playlist:
            abort(404, "Playlist ID: {} doesn't exist".format(playlist_id))
        playlist.title = title
        db.session.add(playlist)
        db.session.commit()
        return {"message": "Playlist renamed successfully"}, 201


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
        "album": fields.Nested(album_fields),
        "artist": fields.Nested(artist_fields),
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
            return {"msg": "No playlists found"}, 200


class PlaylistSongAssociation(Resource):

    @jwt_required()
    def post(self, playlist_id, user_id):
        if user_id != get_jwt_identity():
            abort(403, "You are not authorized to view this profile")
        user = User.query.get(user_id)
        if not user:
            abort(404, "User ID: {} doesn't exist".format(user_id))
        playlist = Playlist.query.get(playlist_id)
        if not playlist:
            abort(404, "Playlist ID: {} doesn't exist".format(playlist_id))

        data = request.json
        song_ids = data.get("song_ids", [])

        print(song_ids)

        for song_id in song_ids:
            song = Song.query.get(song_id)
            if not song:
                abort(404, "Song ID: {} doesn't exist".format(song_id))

            # Create a new association record
            association = playlist_song_association.insert().values(
                playlist_id=playlist_id, song_id=song_id
            )

            # Execute the insertion statement
            db.session.execute(association)
            db.session.commit()

        return {"message": "Song added to playlist successfully"}, 201

    @jwt_required()
    def delete(self, playlist_id, user_id):
        if user_id != get_jwt_identity():
            abort(403, "You are not authorized to view this profile")
        user = User.query.get(user_id)
        if not user:
            abort(404, "User ID: {} doesn't exist".format(user_id))
        playlist = Playlist.query.get(playlist_id)
        if not playlist:
            abort(404, "Playlist ID: {} doesn't exist".format(playlist_id))

        data = request.json
        song_id = data.get("song_id")

        song = Song.query.get(song_id)
        if not song:
            abort(404, "Song ID: {} doesn't exist".format(song_id))

        # Create a new association record
        association = (
            playlist_song_association.delete()
            .where(playlist_song_association.c.playlist_id == playlist_id)
            .where(playlist_song_association.c.song_id == song_id)
        )

        # Execute the insertion statement
        db.session.execute(association)
        db.session.commit()

        return {"message": "Song removed from playlist successfully"}, 200
