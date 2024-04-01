from flask_restful import Resource, reqparse, fields, marshal_with
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import abort
from backend.models import Album, User, db


class AlbumResource(Resource):
    def get(self):
        pass

    @jwt_required()
    def post(self, user_id):
        if user_id != get_jwt_identity():
            abort(403, "You are not authorized to view this profile")
        user = User.query.get(user_id)
        if not user:
            abort(404, "User ID: {} doesn't exist".format(user_id))

        parser = reqparse.RequestParser()
        parser.add_argument(
            "name", type=str, required=True, help="Album name is required"
        )
        parser.add_argument(
            "description", type=str, required=True, help="Album description is required"
        )
        # parser.add_argument(
        #     "imageData", type=str, required=True, help="File field required"
        # )

        args = parser.parse_args()

        if args["name"] == "":
            abort(400, "Album name cannot be empty")
        if args["description"] == "":
            abort(400, "Album description cannot be empty")
        # if args["imageData"] == "":
        #     abort(400, "Album poster cannot be empty")

        # poster_data = args["imageData"]
        album = Album(
            name=args["name"],
            description=args["description"],
            artist_id=user_id,
        )
        db.session.add(album)
        db.session.commit()

        return ({"message": "Album created successfully"}, 201)

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
