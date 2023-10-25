from flask import Blueprint

auth = Blueprint('auth', __name__, url_prefix='/auth')

users = Blueprint('users', __name__, url_prefix='/users')
auth.register_blueprint(users)

from . import views, errors
