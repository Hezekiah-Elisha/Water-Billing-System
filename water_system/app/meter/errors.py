from . import meter
from flask import jsonify
from werkzeug.exceptions import RequestEntityTooLarge


@meter.app_errorhandler(RequestEntityTooLarge)
def handle_file_size_exception(e):
    return jsonify(error='File size exceeds the maximum limit of 4 megabytes'), 413