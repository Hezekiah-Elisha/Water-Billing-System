from flask import Blueprint

supervisor = Blueprint('supervisor', __name__, url_prefix='/supervisors')

from . import views