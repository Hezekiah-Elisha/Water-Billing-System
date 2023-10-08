from flask import Blueprint

customer = Blueprint('customer', __name__, url_prefix='/customers')

from . import views