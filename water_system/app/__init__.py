from flask import Flask

from config import config
from .extensions import db, jwt, cors, ma


def create_app(config_name='default'):
    app = Flask(__name__)

    # config_name = 'development'

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    jwt.init_app(app)
    cors.init_app(app)
    db.init_app(app)
    ma.init_app(app)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .meter import meter as meter_blueprint
    app.register_blueprint(meter_blueprint)

    return app
