from flask import Flask

app = Flask(__name__)

import config

from backend import initial_data

from backend import resources


@app.route("/")
def hello_world():
    return "Hello, World!"


if __name__ == "__main__":
    app.run(debug=True)
