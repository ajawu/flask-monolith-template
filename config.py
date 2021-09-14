"""Flask configuration."""
from decouple import config


class Config:
    """Set Flask config variables."""

    FLASK_ENV = config('ENV')
    TESTING = True
    SECRET_KEY = config('SECRET_KEY')
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'

    # Database
    SQLALCHEMY_DATABASE_URI = config('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
