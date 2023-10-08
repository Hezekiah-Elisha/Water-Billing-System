from flask_marshmallow import Marshmallow as ma
from .Customer import Customer

ma = ma()


class CustomerSchema(ma.Schema):
    class Meta:
        model = Customer
        fields = ('id', 'name', 'phone', 'email', 'location', 'created_at')

        _links = ma.Hyperlinks({
            'self': ma.URLFor('customer_details', values=dict(id='<id>')),
            'collection': ma.URLFor('customers')
        })


customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)