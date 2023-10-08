from flask import Blueprint

worker = Blueprint('worker', __name__, url_prefix='/workers')

from . import views