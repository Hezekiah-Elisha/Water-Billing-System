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


@bill.route('/<int:id>', methods=['GET'])
def get_bill_by_id(id):
    bill = Bill.get_bill_by_id(id)
    if not bill:
        return jsonify(message='Bill not found'), 404
    bill_info = bill_schema.dump(bill)
    return jsonify(bill=bill_info), 200


@bill.route('/', methods=['DELETE'])
def delete_all_bills():
    bills = Bill.get_all_bills()
    if not bills:
        return jsonify(message='No bills found'), 404
    for bill in bills:
        bill.delete()
    return jsonify(message='All bills deleted'), 200