import os


class Config(object):
    """Parent configuration class."""
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET')#TODO:change these env variable names
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SECRET_KEY = 1234