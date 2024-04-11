from flask import Flask, send_from_directory
from flask_cors import CORS
from werkzeug.utils import secure_filename

app = Flask(
    __name__, template_folder="./frontend/templates", static_folder="./backend/static"
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


@app.route("/song/cover/<song_id>")
def song_cover(song_id):
    song = Song.query.get(song_id)
    filename = secure_filename(song.title) + ".jpg"
    return send_from_directory(app.config["UPLOAD_FOLDER_SONG"], filename)


@app.route("/song/audio/<song_id>")
def song_audio(song_id):
    song = Song.query.get(song_id)
    filename = secure_filename(song.title) + ".mp3"
    return send_from_directory(app.config["UPLOAD_FOLDER_AUDIO"], filename)


@app.route("/carousel/<id>")
def carousel(id):
    return send_from_directory(app.static_folder + "/carousel", f"carousel{id}.jpg")


if __name__ == "__main__":
    app.run(debug=True)
