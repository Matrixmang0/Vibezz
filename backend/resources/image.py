from flask import request, abort
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.utils import secure_filename
from backend.models import User

import os

UPLOAD_FOLDER_ALBUM = "./backend/static/album"
UPLOAD_FOLDER_SONG = "./backend/static/song"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}


class ImageAlbum(Resource):

    @jwt_required()
    def post(self, user_id):

        if user_id != get_jwt_identity():
            abort(403, "You are not authorized to make this request")
        user = User.query.get(user_id)
        if not user:
            abort(404, "User ID: {} doesn't exist".format(user_id))

        # check if the post request has the file part
        if "image" not in request.files:
            return {"error": "No file part"}, 400

        file = request.files["image"]

        # if user does not select file, browser also submit an empty part without filename
        if file.filename == "":
            return {"error": "No selected file"}, 400

        title = request.form.get("title")

        if file and self.allowed_file(file.filename):
            # Generate a safe filename based on the album title
            filename = secure_filename(title) + os.path.splitext(file.filename)[1]
            file.save(os.path.join(UPLOAD_FOLDER_ALBUM, filename))
            return {"message": "File uploaded successfully", "filename": filename}, 201

        return {"error": "Invalid file type"}, 400

    def allowed_file(self, filename):
        return (
            "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
        )


class ImageAlbum(Resource):

    @jwt_required()
    def post(self, user_id):

        if user_id != get_jwt_identity():
            abort(403, "You are not authorized to make this request")
        user = User.query.get(user_id)
        if not user:
            abort(404, "User ID: {} doesn't exist".format(user_id))

        # check if the post request has the file part
        if "image" not in request.files:
            return {"error": "No file part"}, 400

        file = request.files["image"]

        # if user does not select file, browser also submit an empty part without filename
        if file.filename == "":
            return {"error": "No selected file"}, 400

        title = request.form.get("title")

        if file and self.allowed_file(file.filename):
            # Generate a safe filename based on the album title
            filename = secure_filename(title) + os.path.splitext(file.filename)[1]
            file.save(os.path.join(UPLOAD_FOLDER_SONG, filename))
            return {"message": "File uploaded successfully", "filename": filename}, 201

        return {"error": "Invalid file type"}, 400

    def allowed_file(self, filename):
        return (
            "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
        )
