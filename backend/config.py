import os
basedir = os.path.abspath(os.path.dirname(__file__))

DB_URL = 'postgresql+psycopg2://walterclayton:secure@localhost/mydatabase'

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'secure'
    SQLALCHEMY_DATABASE_URI = [DB_URL]


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True