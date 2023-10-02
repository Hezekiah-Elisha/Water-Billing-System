from flask import Blueprint

meter = Blueprint('meter', __name__, url_prefix='/meter')

from . import views
