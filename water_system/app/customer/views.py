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