from flask import jsonify, request
from . import billing

@billing.route('/test', methods=['GET'])
def test():
    return jsonify(message='Billing endpoint working'), 200