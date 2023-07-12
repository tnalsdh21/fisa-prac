from flask import Flask 
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    app.config.from_object(config)

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models

    from views import basic_views,soom_views
    app.register_blueprint(basic_views.fisa)
    app.register_blueprint(soom_views.soom)

    return app
