from flask_restful import Api
from app import app
from flask_jwt_extended import JWTManager

jwt = JWTManager(app)

api = Api(app, prefix="/api")

from backend.resources.login import LoginResource

from backend.resources.user import UserResource
from backend.resources.user import UsersResource
from backend.resources.user import PassResource
from backend.resources.user import AdminUserResource

from backend.resources.album import AlbumsResource
from backend.resources.album import UserAlbumResource
from backend.resources.album import LibraryResource
from backend.resources.album import AlbumResource
from backend.resources.album import AlbumName
from backend.resources.album import DeleteAlbumResource
from backend.resources.album import EditAlbumResource

from backend.resources.song import SongsResource
from backend.resources.song import SongResource
from backend.resources.song import SongPageResource
from backend.resources.song import GetSongResource
from backend.resources.song import EditSongResource
from backend.resources.song import DeleteSongResource

from backend.resources.playlist import PlaylistsResource
from backend.resources.playlist import PostPlaylistResource
from backend.resources.playlist import PutPlaylistResource
from backend.resources.playlist import PlaylistResource
from backend.resources.playlist import PlaylistSongAssociation

from backend.resources.ratings import RatingsResource

from backend.resources.flag import FlagResource

from backend.resources.image import ImageAlbum
from backend.resources.image import ImageSong

api.add_resource(LoginResource, "/login")
api.add_resource(UserResource, "/user/<int:user_id>")
api.add_resource(UsersResource, "/users")
api.add_resource(PassResource, "/user/<int:user_id>/edit-pass")
api.add_resource(AdminUserResource, "/user_data")

api.add_resource(AlbumsResource, "/<int:user_id>/albums")
api.add_resource(UserAlbumResource, "/album/<int:album_id>")
api.add_resource(LibraryResource, "/albums")
api.add_resource(AlbumResource, "/<int:user_id>/new-album")
api.add_resource(EditAlbumResource, "/<int:user_id>/edit-album/<int:album_id>")
api.add_resource(AlbumName, "/<int:user_id>/albums/<int:album_id>/info")
api.add_resource(DeleteAlbumResource, "/<int:user_id>/albums/<int:album_id>/delete")

api.add_resource(SongsResource, "/<int:user_id>/album/<int:album_id>")
api.add_resource(SongResource, "/<int:user_id>/song")
api.add_resource(SongPageResource, "/song/<int:song_id>")
api.add_resource(GetSongResource, "/<int:user_id>/songs/<int:song_id>")
api.add_resource(EditSongResource, "/<int:user_id>/edit-song/<int:song_id>")
api.add_resource(DeleteSongResource, "/<int:user_id>/songs/<int:song_id>/delete")

api.add_resource(PlaylistsResource, "/<int:user_id>/playlists")
api.add_resource(PostPlaylistResource, "/<int:user_id>/new-playlist")
api.add_resource(PutPlaylistResource, "/<int:user_id>/edit-playlist/<int:playlist_id>")
api.add_resource(PlaylistResource, "/<int:user_id>/playlist/<int:playlist_id>")
api.add_resource(PlaylistSongAssociation, "/<int:user_id>/<int:playlist_id>/add_songs")

api.add_resource(RatingsResource, "/<int:user_id>/rate/<int:song_id>")

api.add_resource(FlagResource, "/<int:user_id>/flag")

api.add_resource(ImageAlbum, "/<int:user_id>/albums/upload-image")
api.add_resource(ImageSong, "/<int:user_id>/songs/upload-image")
