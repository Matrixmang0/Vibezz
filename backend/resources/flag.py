from flask_restful import Resource, reqparse, fields, marshal, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import abort, request

from backend.models import User, Song, Flags, db


class FlagResource(Resource):

    @jwt_required()
    def post(self, user_id):
        if user_id != get_jwt_identity():
            abort(403, "You are not authorized to view this page")
        user = User.query.get(user_id)
        if not user:
            abort(404, "User ID: {} doesn't exist".format(user_id))

        data = request.get_json()
        song_id = data.get("song_id")
        song = Song.query.get(song_id)
        if not song:
            abort(404, "Song ID: {} doesn't exist".format(song_id))

        ex_flag = Flags.query.filter_by(user_id=user_id, song_id=song_id).first()
        if ex_flag:
            abort(404, "You have already flagged this song")

        flag = Flags(
            user_id=user_id,
            song_id=song_id,
        )

        db.session.add(flag)
        db.session.commit()
        return ({"message": "Song Successfully Flagged"}, 201)


class AdminFlagResource(Resource):

    user_fields = {
        "id": fields.Integer,
        "username": fields.String,
        "name": fields.String,
        "email": fields.String,
    }

    album_fields = {
        "id": fields.Integer,
        "title": fields.String,
        "description": fields.String,
    }

    artist_fields = {
        "id": fields.Integer,
        "name": fields.String,
    }

    song_fields = {
        "id": fields.Integer,
        "title": fields.String,
        "genre": fields.String,
        "lyrics": fields.String,
        "album": fields.Nested(album_fields),
        "artist": fields.Nested(artist_fields),
    }

    flag_fields = {
        "id": fields.Integer,
        "user": fields.Nested(user_fields),
        "song": fields.Nested(song_fields),
    }

    @jwt_required()
    def get(self):
        if get_jwt_identity() == "0":
            abort(403, "You are not authorized to access this information")

        flags = Flags.query.all()
        if not flags:
            return {"msg": "No flags found"}, 200
        flags = [marshal(flag, self.flag_fields) for flag in flags]
        return flags, 200


class AdminDeleteFlagResource(Resource):

    @jwt_required()
    def delete(self, flag_id):
        if get_jwt_identity() == "0":
            abort(403, "You are not authorized to access this information")

        flag = Flags.query.filter_by(id=flag_id).first()
        if not flag:
            abort(404, "Flag ID: {} doesn't exist".format(flag_id))
        db.session.delete(flag)
        db.session.commit()
        return ({"message": "Flag Successfully Deleted"}, 200)
