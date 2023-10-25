from flask import Blueprint

meter = Blueprint('meter', __name__, url_prefix='/meters')
readings = Blueprint('readings', __name__, url_prefix='/readings')
meter.register_blueprint(readings)

from . import views
