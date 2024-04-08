from flask_restful import Api
from app import app
from flask_jwt_extended import JWTManager

jwt = JWTManager(app)

api = Api(app, prefix="/api")

from backend.resources.login import LoginResource

from backend.resources.user import UserResource
from backend.resources.user import UsersResource
from backend.resources.user import PassResource

from backend.resources.album import AlbumsResource
from backend.resources.album import AlbumResource
from backend.resources.album import DeleteAlbumResource

from backend.resources.image import ImageAlbum
from backend.resources.image import ImageSong

api.add_resource(LoginResource, "/login")
api.add_resource(UserResource, "/user/<int:user_id>")
api.add_resource(UsersResource, "/users")
api.add_resource(PassResource, "/user/<int:user_id>/edit-pass")

api.add_resource(AlbumsResource, "/<int:user_id>/albums")
api.add_resource(AlbumResource, "/<int:user_id>/new-album")
api.add_resource(DeleteAlbumResource, "/<int:user_id>/albums/<int:album_id>/delete")

api.add_resource(ImageAlbum, "/<int:user_id>/albums/upload-image")
api.add_resource(ImageSong, "/<int:user_id>/albums/upload-image")
