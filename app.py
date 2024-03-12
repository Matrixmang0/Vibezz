from flask import Flask
from backend.models import db
from config import DevelopmentConfig
from backend.resources import api


def create_app():
  app = Flask(__name__)
  app.config.from_object(DevelopmentConfig)
  db.init_app(app)
  api.init_app(app)
  with app.app_context():
    import backend.views

  return app


app = create_app()

if __name__ == '__main__':
  app.run(debug=True)
