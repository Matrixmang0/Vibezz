from flask import Flask, send_from_directory
from flask_cors import CORS
from werkzeug.utils import secure_filename
from celery_worker import make_celery
from celery.schedules import crontab
import time
from httplib2 import Http
from json import dumps
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from flask_caching import Cache


def send_email(to_addess, subject, message, content="text", attachment_file=None):

    msg = MIMEMultipart()
    msg["From"] = "auto-emails@vibezz.com"
    msg["To"] = to_addess
    msg["Subject"] = subject

    if content == "html":
        msg.attach(MIMEText(message, "html"))
    else:
        msg.attach(MIMEText(message, "plain"))

    if attachment_file:
        with open(attachment_file, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header(
                "Content-Disposition", f"attachment; filename={attachment_file}"
            )
            msg.attach(part)

    server = smtplib.SMTP(host="localhost", port=1025)
    server.login("auto-emails@vibezz.com", "")
    server.send_message(msg)
    server.quit()
    return True


app = Flask(
    __name__, template_folder="./frontend/templates", static_folder="./backend/static"
)
cors = CORS(app, resources={r"/api/*": {"origins": "http://localhost:8080"}})

import config

celery = make_celery(app)

cache = Cache(app)

app.app_context().push()


@celery.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # sender.add_periodic_task(crontab(hour=17, minute=0), send_remainder.s(), name="daily remainder")
    sender.add_periodic_task(60, send_remainder.s(), name="daily remainder")
    # sender.add_periodic_task(
    #     crontab(day_of_month=1, hour=8, minute=0),
    #     send_report_email.s(),
    #     name="monthly report for creators",
    # )
    sender.add_periodic_task(
        60,
        send_report_email.s(),
        name="monthly report for creators",
    )


@celery.task()
def send_remainder():

    url = "https://chat.googleapis.com/v1/spaces/AAAAfhT2gF8/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=i1Q9cNN_XA3_L0_EbZJHoD6A-0-HNtOBguqknCuPT4Q"
    bot_message = {
        "text": """Hey there! How was your day?\nDon't forget to check out the new albums and songs that have been added to the library today!
"""
    }
    message_headers = {"Content-Type": "application/json; charset=UTF-8"}
    http_obj = Http()
    response = http_obj.request(
        uri=url,
        method="POST",
        headers=message_headers,
        body=dumps(bot_message),
    )
    print(response)
    return "Remainder will be sent every 60 seconds"


@celery.task()
def send_report_email():
    with app.app_context():
        artists = User.query.filter_by(role_id="art").all()
        for artist in artists:
            send_email(
                to_addess=artist.email,
                subject="Monthly Report",
                message=f"Dear {artist.name},\nPlease find the attached report for the past month",
                content="text/html",
                attachment_file="./monthly_report/report.pdf",
            )
        return "Email scheduled for creators"


from backend import initial_data

from backend import resources

from backend.models import Album, Song, User, db


@cache.cached(timeout=60)
@app.route("/album/<album_id>")
def album_cover(album_id):
    album = Album.query.get(album_id)
    filename = secure_filename(album.title) + ".jpg"
    return send_from_directory(app.config["UPLOAD_FOLDER_ALBUM"], filename)


@cache.cached(timeout=60)
@app.route("/song/cover/<song_id>")
def song_cover(song_id):
    song = Song.query.get(song_id)
    filename = secure_filename(song.title) + ".jpg"
    return send_from_directory(app.config["UPLOAD_FOLDER_SONG"], filename)


@cache.cached(timeout=60)
@app.route("/song/audio/<song_id>")
def song_audio(song_id):
    song = Song.query.get(song_id)
    filename = secure_filename(song.title) + ".mp3"
    return send_from_directory(app.config["UPLOAD_FOLDER_AUDIO"], filename)


@cache.cached(timeout=60)
@app.route("/carousel/<id>")
def carousel(id):
    return send_from_directory(app.static_folder + "/carousel", f"carousel{id}.jpg")


if __name__ == "__main__":
    app.run(debug=True)
