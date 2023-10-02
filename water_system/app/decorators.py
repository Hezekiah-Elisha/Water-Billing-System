from flask_jwt_extended import get_jwt_identity
from .auth.models.User import User

def admin_required(fn):
    def wrapper(*args, **kwargs):
        current_user = get_jwt_identity()
        user = User.get_user_role_by_email(current_user)
        # user = User.get_user_by_email(current_user).role
        if not user or user != 'admin':
            return {'message': 'Admins only!'}, 403
        return fn(*args, **kwargs)
    return wrapper

def supervisor_required(fn):
    def wrapper(*args, **kwargs):
        current_user = get_jwt_identity()
        user = User.get_user_by_email(current_user).role
        if not user or user != 'supervisor':
            return {'message': 'Supervisors only!'}, 403
        return fn(*args, **kwargs)
    return wrapper

# worker required
def worker_required(fn):
    def wrapper(*args, **kwargs):
        current_user = get_jwt_identity()
        user = User.get_user_by_email(current_user).role
        if not user or user != 'worker':
            return {'message': 'Workers only!'}, 403
        return fn(*args, **kwargs)
    return wrapper