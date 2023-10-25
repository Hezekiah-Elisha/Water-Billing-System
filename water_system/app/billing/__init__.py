from flask import Blueprint

bill = Blueprint('bill', __name__, url_prefix='/bills')

from . import views