from flask_restful import Resource, reqparse, fields, marshal, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import abort, request

from backend.models import User, Song, Ratings, db


class RatingsResource(Resource):

    @jwt_required()
    def post(self, user_id, song_id):
        if user_id != get_jwt_identity():
            abort(403, "You are not authorized to view this page")
        user = User.query.get(user_id)
        if not user:
            abort(404, "User ID: {} doesn't exist".format(user_id))
        song = Song.query.get(song_id)
        if not song:
            abort(404, "Song ID: {} doesn't exist".format(song_id))

        data = request.get_json()
        rating = data.get("rating")

        ex_rating = Ratings.query.filter_by(user_id=user_id, song_id=song_id).first()
        if ex_rating:
            ex_rating.rating = rating
            db.session.commit()
            return ({"message": "Ratings successfully updated"}, 200)

        ratings = Ratings(
            rating=rating,
            user_id=user_id,
            song_id=song_id,
        )

        song.tot_ratings = (song.tot_ratings + rating) / 2
        song.no_ratings += 1

        db.session.add(ratings)
        db.session.add(song)
        db.session.commit()
        return ({"message": "Ratings successfully posted"}, 201)
