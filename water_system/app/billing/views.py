from flask import jsonify, request
from . import bill
from .models.Bill import Bill
from .models.MaBills import bill_schema, bills_schema

@bill.route('/test', methods=['GET'])
def test():
    return jsonify(message='Billing endpoint working'), 200


@bill.route('/', methods=['GET'])
def get_all_bills():
    bills = Bill.get_all_bills()
    if not bills:
        return jsonify(message='No bills found'), 404
    bills_info = bills_schema.dump(bills)
    return jsonify(bills=bills_info), 200