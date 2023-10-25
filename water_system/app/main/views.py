from . import main
from flask import jsonify, request


@main.route('/')
def home():
    return jsonify(message='Welcome to the Water Billing System API')


@main.route('/version', methods=['GET'])
def version():
    return jsonify(version="version 1")
