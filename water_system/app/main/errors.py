from . import main
from flask import jsonify


@main.app_errorhandler(404)
def page_not_found(e):
    response = jsonify({'error': 'Resource not found'})
    response.status_code = 404
    return response


@main.app_errorhandler(500)
def internal_server_error(e):
    response = jsonify({'error': 'Internal Server Error'})
    response.status_code = 500
    return response
