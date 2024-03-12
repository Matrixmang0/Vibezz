from flask_sqlalchemy import SQLAlchemy
from app import app

db = SQLAlchemy(app)

playlist_song_association = db.Table(
    "playlist_song_association",
    db.Column("playlist_id", db.Integer, db.ForeignKey("playlist.id")),
    db.Column("song_id", db.Integer, db.ForeignKey("song.id")),
)


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(15), unique=True, nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    profile_img = db.Column(db.String, nullable=False, default="default.png")
    role_id = db.Column(db.String, db.ForeignKey("role.id"))
    role = db.relationship("Role")
    playlists = db.relationship(
        "Playlist", cascade="all, delete-orphan", backref="user", lazy=True
    )
    created_albums = db.relationship(
        "Album", cascade="all, delete-orphan", backref="artist", lazy=True
    )


class Role(db.Model):
    __tablename__ = "role"
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(100), nullable=False)


class Album(db.Model):
    __tablename__ = "album"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Unicode, nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    poster = db.Column(db.String, nullable=False)
    tot_ratings = db.Column(db.Integer, nullable=False)
    no_ratings = db.Column(db.Integer, nullable=False)
    songs = db.relationship(
        "Song", cascade="all, delete-orphan", backref="album", lazy=True
    )


class Song(db.Model):
    __tablename__ = "song"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Unicode, nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    album_id = db.Column(db.Integer, db.ForeignKey("album.id"), nullable=False)
    lyrics = db.Column(db.Unicode, nullable=False)
    audio = db.Column(db.String, nullable=False)
    poster = db.Column(db.String, nullable=False)
    genre = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.String(100), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False)
    tot_ratings = db.Column(db.Integer, nullable=False)
    no_ratings = db.Column(db.Integer, nullable=False)
    artist = db.relationship("User", lazy=True)


class Playlist(db.Model):
    __tablename__ = "playlist"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False)
    songs = db.relationship(
        "Song", secondary=playlist_song_association, backref="playlist", lazy=True
    )
