from app import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

playlist_song_association = db.Table(
    'playlist_song_association',
    db.Column('playlist_id', db.Integer, db.ForeignKey('playlist.id')),
    db.Column('song_id', db.Integer, db.ForeignKey('song.id'))
)


class Admin(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  username = db.Column(db.String(15), unique=True, nullable=False)
  email = db.Column(db.String(50), unique=True, nullable=False)
  password = db.Column(db.String(100), nullable=False)


class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  username = db.Column(db.String(15), unique=True, nullable=False)
  email = db.Column(db.String(50), nullable=False, unique=True)
  password = db.Column(db.String, nullable=False)
  playlists = db.relationship('Playlist', cascade="all, delete-orphan", backref='user', lazy=True)


class Artist(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  username = db.Column(db.String(15), unique=True, nullable=False)
  email = db.Column(db.String(50), nullable=False, unique=True)
  password = db.Column(db.String, nullable=False)
  albums = db.relationship('Album', cascade="all, delete-orphan", backref='artist', lazy=True)


class Album(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.Unicode, nullable=False)
  artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'), nullable=False)
  poster = db.Column(db.String, nullable=False)
  tot_ratings = db.Column(db.Integer, nullable=False)
  no_ratings = db.Column(db.Integer, nullable=False)
  artist = db.relationship('Artist', cascade="all, delete-orphan", backref="album", lazy=True)
  songs = db.relationship('Song', cascade="all, delete-orphan", backref="songs", lazy=True)


class Song(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.Unicode, nullable=False)
  artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'), nullable=False)
  album_id = db.Column(db.Integer, db.ForeignKey('album.id'), nullable=False)
  lyrics = db.Column(db.Unicode, nullable=False)
  audio = db.Column(db.String, nullable=False)
  poster = db.Column(db.String, nullable=False)
  genre = db.Column(db.String(100), nullable=False)
  duration = db.Column(db.String(100), nullable=False)
  date_created = db.Column(db.DateTime, nullable=False)
  tot_ratings = db.Column(db.Integer, nullable=False)
  no_ratings = db.Column(db.Integer, nullable=False)
  artist = db.relationship('Artist', cascade="all, delete-orphan", backref="song", lazy=True)
  album = db.relationship('Album', backref="song", lazy=True

class Playlist(db.model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(100), nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
  date_created = db.Column(db.DateTime, nullable=False)
  songs = db.relationship('Song', secondary=playlist_song_association, back_populates='playlists')


with app.app_context():
  db.create_all()

  is_admin_present = db.sessio.query(Admin.id).first() is not None
  if not is_admin_present:
    admin = Admin(
      id=1
      name="Admin", 
      username="admin01",
      email="admin01@vibezz.com", 
      password="admin"
    )  
    db.session.add(admin)
    db.session.commit()
    print("Admin created")
