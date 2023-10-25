from flask import Flask

from config import config
from .extensions import db, jwt, cors, ma, bcrypt


def create_app(config_name='default'):
    app = Flask(__name__)
    app.url_map.strict_slashes = False

    # config_name = 'development'

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    jwt.init_app(app)
    cors.init_app(app, supports_credentials=True)
    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)

    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .billing import bill as bill_blueprint
    app.register_blueprint(bill_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .meter import meter as meter_blueprint
    app.register_blueprint(meter_blueprint)

    from .customer import customer as customer_blueprint
    app.register_blueprint(customer_blueprint)

    from .supervisor import supervisor as supervisor_blueprint
    app.register_blueprint(supervisor_blueprint)

    from .worker import worker as worker_blueprint
    app.register_blueprint(worker_blueprint)

    from .notifications import notification as notification_blueprint
    app.register_blueprint(notification_blueprint)

    return app
