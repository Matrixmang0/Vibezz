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
