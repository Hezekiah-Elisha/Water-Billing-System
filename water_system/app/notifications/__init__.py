from flask import Blueprint

notification = Blueprint('notification', __name__, url_prefix='/notifications')

from . import views