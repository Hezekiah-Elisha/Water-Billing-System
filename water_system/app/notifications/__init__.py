from flask import Blueprint

notification = Blueprint('notifications', __name__, url_prefix='/notifications')

from . import views