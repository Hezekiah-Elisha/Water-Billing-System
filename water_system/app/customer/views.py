from flask import request, jsonify
from . import customer
from .models.Customer import Customer
from .models.MaCustomer import customer_schema, customers_schema
from werkzeug.utils import secure_filename

@customer.route('/', methods=['GET'])
def get_all_customers():
    customers = Customer.get_all_customers()
    if not customers:
        return jsonify(message='No customers found'), 404
    result = customers_schema.dump(customers)
    return jsonify(result), 200

@customer.route('/test', methods=['GET'])
def test():
    return jsonify(message='Customer endpoint working'), 200

@customer.route('/', methods=['POST'])
def create_customer():
    data = request.get_json()
    customer = Customer(**data)
    customer.save()
    result = customer_schema.dump(customer)
    return jsonify(result), 201

@customer.route('/<int:id>', methods=['GET'])
def get_customer_by_id(id):
    customer = Customer.get_customer_by_id(id)
    if not customer:
        return jsonify(message='Customer not found'), 404
    result = customer_schema.dump(customer)
    return jsonify(result), 200

@customer.route('/<int:id>', methods=['PUT'])
def update_customer_by_id(id):
    customer = Customer.get_customer_by_id(id)
    if not customer:
        return jsonify(message='Customer not found'), 404
    data = request.get_json()
    for key, value in data.items():
        setattr(customer, key, value)
    customer.update()
    return jsonify(message='Customer updated successfully'), 200

@customer.route('/<int:id>', methods=['DELETE'])
def delete_customer_by_id(id):
    customer = Customer.get_customer_by_id(id)
    if not customer:
        return jsonify(message='Customer not found'), 404
    customer.delete()
    return jsonify(message='Customer deleted successfully'), 200

@customer.route('/<string:phone>', methods=['GET'])
def get_customer_by_phone(phone):
    customer = Customer.get_customer_by_phone(phone)
    if not customer:
        return jsonify(message='Customer not found'), 404
    result = customer_schema.dump(customer)
    return jsonify(result), 200

@customer.route('/<string:email>', methods=['GET'])
def get_customer_by_email(email):
    customer = Customer.get_customer_by_email(email)
    if not customer:
        return jsonify(message='Customer not found'), 404
    result = customer_schema.dump(customer)
    return jsonify(result), 200