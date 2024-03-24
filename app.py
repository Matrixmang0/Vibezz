from flask import Flask, render_template
from flask_cors import CORS

app = Flask(
    __name__, template_folder="./frontend/templates", static_folder="./frontend/static"
)
cors = CORS(app, resources={r"/api/*": {"origins": "http://localhost:8080"}})

import config

from backend import initial_data

from backend import resources


@app.route("/")
def hello_world():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
