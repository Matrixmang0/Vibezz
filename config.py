def Config(object):
  DEBUG = False
  WTF_CSRF_ENABLED = False

def DevelopmentConfig(Config):
  DEBUG = True
  SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'
  SECRET_KEY = 'secret'
  SQLALCHEMY_TRACK_MODIFICATIONS = False