from dotenv import load_dotenv
import os

from app import app

load_dotenv()

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = os.getenv(
    "SQLALCHEMY_TRACK_MODIFICATIONS"
)
app.config["UPLOAD_FOLDER_ALBUM"] = os.getenv("UPLOAD_FOLDER_ALBUM")
app.config["UPLOAD_FOLDER_SONG"] = os.getenv("UPLOAD_FOLDER_SONG")
app.config["UPLOAD_FOLDER_AUDIO"] = os.getenv("UPLOAD_FOLDER_AUDIO")
app.config["ALLOWED_EXTENSIONS_IMAGE"] = os.getenv("ALLOWED_EXTENSIONS_IMAGE")
app.config["ALLOWED_EXTENSIONS_AUDIO"] = os.getenv("ALLOWED_EXTENSIONS_AUDIO")

app.config["CELERY_BROKER_URL"] = os.getenv("CELERY_BROKER_URL")
app.config["CELERY_RESULT_BACKEND"] = os.getenv("CELERY_RESULT_BACKEND")

app.config["CACHE_TYPE"] = os.getenv("CACHE_TYPE")
app.config["CACHE_DEFAULT_TIMEOUT"] = os.getenv("CACHE_DEFAULT_TIMEOUT")
app.config["CACHE_REDIS_URL"] = os.getenv("CACHE_REDIS_URL")

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
