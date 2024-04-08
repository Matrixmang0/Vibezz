from flask import Flask, send_from_directory
from flask_cors import CORS
from werkzeug.utils import secure_filename

app = Flask(
    __name__, template_folder="./frontend/templates", static_folder="./frontend/static"
)
cors = CORS(app, resources={r"/api/*": {"origins": "http://localhost:8080"}})

import config

from backend import initial_data

from backend import resources

from backend.models import Album, Song


@app.route("/album/<album_id>")
def album_cover(album_id):
    album = Album.query.get(album_id)
    filename = secure_filename(album.title) + ".jpg"
    return send_from_directory(app.config["UPLOAD_FOLDER_ALBUM"], filename)


if __name__ == "__main__":
    app.run(debug=True)
