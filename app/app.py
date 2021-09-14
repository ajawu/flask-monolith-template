from celery import Celery
from flask import Flask
from werkzeug.debug import DebuggedApplication
from app.extensions import db, migrate
from app.models import *


def create_celery_app(flask_app: Flask):
    """
    Create a new Celery object and tie together the Celery config to the app's
    config. Wrap all tasks in the context of the application.
    :param flask_app: Flask app
    :return: Celery app
    """
    flask_app = flask_app or create_app()

    celery = Celery(flask_app.import_name)
    celery.conf.update(flask_app.config.get('CELERY_CONFIG', {}))
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with flask_app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask
    return celery


def create_app(settings_override=None):
    """
    Create a Flask application using the app factory pattern.
    :param settings_override: Override settings
    :return: Flask app
    """
    app = Flask(__name__, static_folder='static', static_url_path='')

    app.config.from_object('config.Config')

    if settings_override:
        app.config.update(settings_override)

    load_blueprints(app)
    load_extensions(app)

    if app.debug:
        app.wsgi_app = DebuggedApplication(app.wsgi_app, evalex=True)

    return app


def load_blueprints(flask_app: Flask) -> None:
    """
    Register all flask blueprints
    :param flask_app: Flask application instance
    :return: None
    """
    from app import blueprints
    """
    **************** SAMPLE BLUEPRINT REGISTER ****************
    *   flask_app.register_blueprint(blueprints.{blueprint_name})   *
    ***********************************************************
    """
    flask_app.register_blueprint(blueprints.page)


def load_extensions(flask_app: Flask) -> None:
    """
    Register 0 or more extensions (mutates the app passed in).
    :param flask_app: Flask application instance
    :return: None
    """
    db.init_app(flask_app)
    migrate.init_app(flask_app, db)


# celery_app = create_celery_app()
app = create_app()
