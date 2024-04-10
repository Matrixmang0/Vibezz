from flask import request, abort
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.utils import secure_filename
from backend.models import User

import os

from app import app


class ImageAlbum(Resource):

    @jwt_required()
    def post(self, user_id):

        if user_id != get_jwt_identity():
            abort(403, "You are not authorized to make this request")
        user = User.query.get(user_id)
        if not user:
            abort(404, "User ID: {} doesn't exist".format(user_id))

        if "image" not in request.files:
            return {"error": "No file part"}, 400

        file = request.files["image"]

        if file.filename == "":
            return {"error": "No selected file"}, 400

        title = request.form.get("title")

        if file and self.allowed_file(file.filename):
            filename = secure_filename(title) + os.path.splitext(file.filename)[1]
            file.save(os.path.join(app.config["UPLOAD_FOLDER_ALBUM"], filename))
            return {"message": "File uploaded successfully", "filename": filename}, 201

        return {"error": "Invalid file type"}, 400

    def allowed_file(self, filename):
        return (
            "." in filename
            and filename.rsplit(".", 1)[1].lower()
            in app.config["ALLOWED_EXTENSIONS_IMAGE"]
        )


class ImageSong(Resource):

    @jwt_required()
    def post(self, user_id):

        if user_id != get_jwt_identity():
            abort(403, "You are not authorized to make this request")
        user = User.query.get(user_id)
        if not user:
            abort(404, "User ID: {} doesn't exist".format(user_id))

        # check if the post request has the file part
        if "image" not in request.files:
            return {"error": "No image file"}, 400

        if "audio" not in request.files:
            return {"error": "No audio file"}, 400

        image = request.files["image"]
        audio = request.files["audio"]

        # if user does not select file, browser also submit an empty part without filename
        if image.filename == "":
            return {"error": "No selected image file"}, 400

        if audio.filename == "":
            return {"error": "No selected audio file"}, 400

        title = request.form.get("title")

        if (
            image
            and self.allowed_file_image(image.filename)
            and audio
            and self.allowed_file_audio(audio.filename)
        ):
            # Generate a safe filename based on the album title
            filename1 = secure_filename(title) + os.path.splitext(image.filename)[1]
            filename2 = secure_filename(title) + os.path.splitext(audio.filename)[1]
            image.save(os.path.join(app.config["UPLOAD_FOLDER_SONG"], filename1))
            audio.save(os.path.join(app.config["UPLOAD_FOLDER_AUDIO"], filename2))
            return {
                "message": "Image and Audio file uploaded successfully",
                "filename1": filename1,
                "filename": filename2,
            }, 201

        return {"error": "Invalid file type"}, 400

    def allowed_file_image(self, filename):
        return (
            "." in filename
            and filename.rsplit(".", 1)[1].lower()
            in app.config["ALLOWED_EXTENSIONS_IMAGE"]
        )

    def allowed_file_audio(self, filename):
        return (
            "." in filename
            and filename.rsplit(".", 1)[1].lower()
            in app.config["ALLOWED_EXTENSIONS_AUDIO"]
        )
