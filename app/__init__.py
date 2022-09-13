import os
import redis

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session

import config

db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()

REDIS_SERVER = os.getenv('REDIS_SERVER')

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    app.config['SECRET_KEY'] = 'testtesttest'


    app.config['SESSION_TYPE'] = 'redis'
    app.config['SESSION_PERMANENT'] = False
    app.config['SESSION_USE_SIGNER'] = True
    app.config['SESSION_REDIS'] = redis.from_url(REDIS_SERVER)

    server_session = Session(app)

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models

    from .views import login_views
    app.register_blueprint(login_views.bp)

    return app