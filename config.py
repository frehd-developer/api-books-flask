class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///books.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    SECRET_KEY = "myultrasecretkeyforproduction"


class DevelopmentConfig(Config):
    ENV = "development"
    SECRET_KEY = "myultrasecretkey"
    DEBUG = True
    SERVER_NAME = "localhost:5500"


class TestConfig(Config):
    TESTING = True