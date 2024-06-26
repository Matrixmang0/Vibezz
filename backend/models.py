from flask_sqlalchemy import SQLAlchemy
from app import app
from werkzeug.security import generate_password_hash, check_password_hash

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
    passhash = db.Column(db.String, nullable=False)

    @property
    def password(self):
        raise AttributeError("Password is not a readable attribute")

    def set_password(self, password):
        self.passhash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.passhash, password)

    role_id = db.Column(db.String, db.ForeignKey("role.id"), default="usr")
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
    description = db.Column(db.String, nullable=False)
    tot_ratings = db.Column(db.Integer, nullable=False, default=0)
    no_ratings = db.Column(db.Integer, nullable=False, default=0)
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
    genre = db.Column(db.String(100), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False)
    tot_ratings = db.Column(db.Integer, nullable=False, default=0)
    no_ratings = db.Column(db.Integer, nullable=False, default=0)
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


class Flags(db.Model):
    __tablename__ = "flags"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    song_id = db.Column(db.Integer, db.ForeignKey("song.id"), nullable=False)
    user = db.relationship("User", lazy=True)
    song = db.relationship("Song", lazy=True)
    __table_args__ = (db.UniqueConstraint("user_id", "song_id", name="unique_flag"),)


class Ratings(db.Model):
    __tablename__ = "ratings"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    song_id = db.Column(db.Integer, db.ForeignKey("song.id"), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    user = db.relationship("User", lazy=True)
    song = db.relationship("Song", lazy=True)
    __table_args__ = (db.UniqueConstraint("user_id", "song_id", name="unique_rating"),)
