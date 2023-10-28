from flask import request, jsonify
from . import auth, users
from .models.User import User
from .models.TokenBlocklist import TokenBlocklist
from .models.MaUser import user_schema, users_schema
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, get_jwt
from werkzeug.security import generate_password_hash, check_password_hash
from .. import jwt
from datetime import datetime, timedelta, timezone
from ..decorators import admin_required


@auth.route('/', methods=['GET'])
def hello_world():
    return jsonify(message='Welcome to the Auth Route')


@auth.route('/login', methods=['POST'])
def login():
    email = request.json.get('email', None)
    password = request.json.get('password', None)

    if not email:
        return jsonify(message='Email is required'), 400
    if not password:
        return jsonify(message='Password is required'), 400

    user = User.get_user_by_email(email)

    if not user:
        return jsonify(message='User not found'), 404

    if not check_password_hash(user.password, password):
        return jsonify(message='Incorrect password'), 400

    access_token = create_access_token(identity=user.email)

    user_info = user_schema.dump(user)

    return jsonify(access_token=access_token, user=user_info), 200


# register user
@auth.route('/', methods=['POST'])
def register():
    username = request.json.get('username', None)
    email = request.json.get('email', None)
    password = request.json.get('password', None)
    role = request.json.get('role', None)

    if not username:
        return jsonify(message='Username is required'), 400
    if not email:
        return jsonify(message='Email is required'), 400
    if not password:
        return jsonify(message='Password is required'), 400
    if not role:
        return jsonify(message='Role is required'), 400

    hashed_password = generate_password_hash(password, method='sha256')

    new_user = User(
        username=username,
        email=email,
        password=hashed_password,
        role=role)

    feedback = new_user.save()

    if not feedback:
        return jsonify(message='User already exists'), 400
    
    # get all users
    users = User.get_all_users()
    result = users_schema.dump(users)

    return jsonify(message='User created successfully', users=result), 201


@auth.route("/logout", methods=["DELETE"])
@jwt_required()
def modify_token():
    jti = get_jwt()["jti"]
    now = datetime.now(timezone.utc)

    TokenBlocklistInfo = TokenBlocklist(jti=jti, created_at=now)
    TokenBlocklistInfo.save()

    return jsonify(msg="JWT revoked")


@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload: dict) -> bool:
    jti = jwt_payload["jti"]

    token = TokenBlocklist.get_token_by_id(jti)

    return token is not None


@users.route('/', methods=['GET'])
def get_all_users():
    users = User.get_all_users()
    if not users:
        return jsonify(message='No users found'), 404
    result = users_schema.dump(users)
    return jsonify(result)


@users.route('/', methods=['DELETE'])
def delete_all_users():
    users = User.get_all_users()
    if not users:
        return jsonify(message='No users found'), 404
    User.delete_all_users()
    return jsonify(message='All users deleted successfully'), 200


@auth.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200


@users.route('/<int:id>', methods=['GET'])
# @jwt_required()
def get_user_by_id(id):
    user = User.get_user_by_id(id)
    if not user:
        return jsonify(message='User not found'), 404
    result = user_schema.dump(user)
    return jsonify(result)


@users.route('/<int:id>', methods=['PUT'])
@jwt_required()
def update_user(id):
    user = User.get_user_by_id(id)
    if not user:
        return jsonify(message='User not found'), 404
    username = request.json.get('username', None)
    email = request.json.get('email', None)
    role = request.json.get('role', None)

    if not username:
        return jsonify(message='Username is required'), 400
    if not email:
        return jsonify(message='Email is required'), 400
    if not role:
        return jsonify(message='Role is required'), 400

    user.username = username
    user.email = email
    user.role = role

    user.update()

    return jsonify(message='User updated successfully'), 200


@users.route('/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.get_user_by_id(id)
    if not user:
        return jsonify(message='User not found'), 404
    user.delete()

    # get all users
    users = User.get_all_users()
    result = users_schema.dump(users)
    return jsonify(message='User deleted successfully', users = result), 200


@users.route('/<int:id>/password', methods=['PUT'])
@jwt_required()
def update_user_password(id):
    user = User.get_user_by_id(id)
    if not user:
        return jsonify(message='User not found'), 404
    password = request.json.get('password', None)

    if not password:
        return jsonify(message='Password is required'), 400

    hashed_password = generate_password_hash(password, method='sha256')
    user.password = hashed_password

    user.update()

    return jsonify(message='Password updated successfully'), 200


@users.route('/<int:id>/role', methods=['PUT'])
@jwt_required()
def update_user_role(id):
    user = User.get_user_by_id(id)
    if not user:
        return jsonify(message='User not found'), 404
    role = request.json.get('role', None)

    if not role:
        return jsonify(message='Role is required'), 400

    user.role = role

    user.update()

    return jsonify(message='Role updated successfully'), 200


@users.route('/<int:id>/username', methods=['PUT'])
@jwt_required()
def update_user_username(id):
    user = User.get_user_by_id(id)
    if not user:
        return jsonify(message='User not found'), 404
    username = request.json.get('username', None)

    if not username:
        return jsonify(message='Username is required'), 400

    user.username = username

    user.update()

    return jsonify(message='Username updated successfully'), 200


@users.route('/<int:id>/email', methods=['PUT'])
@jwt_required()
def update_user_email(id):
    user = User.get_user_by_id(id)
    if not user:
        return jsonify(message='User not found'), 404
    email = request.json.get('email', None)

    if not email:
        return jsonify(message='Email is required'), 400

    user.email = email

    user.update()

    return jsonify(message='Email updated successfully'), 200


@users.route('/<int:id>/username', methods=['GET'])
def get_user_username(id):
    user = User.get_user_by_id(id)
    if not user:
        return jsonify(message='User not found'), 404
    return jsonify(username=user.username), 200


@users.route('/<int:id>/email', methods=['GET'])
@jwt_required()
def get_user_email(id):
    user = User.get_user_by_id(id)
    if not user:
        return jsonify(message='User not found'), 404
    return jsonify(email=user.email), 200


@users.route('/<int:id>/role', methods=['GET'])
@jwt_required()
def get_user_role(id):
    user = User.get_user_by_id(id)
    if not user:
        return jsonify(message='User not found'), 404
    return jsonify(role=user.role), 200


@users.route('/@<string:username>', methods=['GET'])
@jwt_required()
def get_user_by_username(username):
    user = User.get_user_by_username(username)
    if not user:
        return jsonify(message='User not found'), 404
    result = user_schema.dump(user)
    return jsonify(result)


@users.route('/profile', methods=['GET'])
@jwt_required()
def get_user_profile():
    email = get_jwt_identity()
    user = User.get_user_by_email(email)
    if not user:
        return jsonify(message='User not found'), 404
    result = user_schema.dump(user)
    return jsonify(result)


@users.route('/username', methods=['GET'])
@jwt_required()
def get_username():
    email = get_jwt_identity()
    username = User.get_username(email)
    if not username:
        return jsonify(message='User not found'), 404
    return jsonify(username=username), 200

# verify email


@users.route('/<string:verification_code>/verify', methods=['GET'])
def verify_user(verification_code):
    user = User.verify_user(verification_code)
    if not user:
        return jsonify(message='User not found'), 404
    return jsonify(message='User verified successfully'), 200


@auth.route('/for-admins-only', methods=['GET'])
@jwt_required()
@admin_required
def for_admins_only():
    return jsonify(message='Admins only!'), 200


@auth.route('/for-users-only', methods=['GET'])
@jwt_required()
def for_users_only():
    return jsonify(message='Users only!'), 200


@auth.route('/users/role/<string:role>', methods=['GET'])
def get_user_by_role(role):
    users = User.get_users_by_role(role)
    if not users:
        return jsonify(message='Users in role not found'), 404
    result = users_schema.dump(users)
    return jsonify(result)


@users.route('/role/<string:role>', methods=['GET'])
def get_users_by_role(role):
    users = User.get_users_by_role(role)
    if not users:
        return jsonify(message='Users in role not found'), 404
    result = users_schema.dump(users)
    return jsonify(result)