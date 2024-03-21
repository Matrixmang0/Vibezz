from flask import Flask, render_template

app = Flask(
    __name__, template_folder="./frontend/templates", static_folder="./frontend/static"
)

import config

from backend import initial_data

from backend import resources


@app.route("/")
def hello_world():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
