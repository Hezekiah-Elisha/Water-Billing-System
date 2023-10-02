from flask import jsonify, request
from . import meter
from flask_jwt_extended import jwt_required
from ..decorators import admin_required, supervisor_required, worker_required


@meter.route('/')
def index():
    return jsonify(message='Hello from meter!')


@meter.route('/', methods=['POST'])
@jwt_required()
@admin_required
def create_meter():
    return jsonify(message='Create meter!')
