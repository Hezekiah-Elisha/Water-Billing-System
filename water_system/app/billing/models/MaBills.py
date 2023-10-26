from flask_marshmallow import Marshmallow as ma
from flask_marshmallow import fields

from .Bill import Bill

ma = ma()


class BillSchema(ma.Schema):
    class Meta:
        model = Bill
        fields = ('id', 'meter_id', 'units', 'amount','status', 'created_at')

        _links = ma.Hyperlinks({
            'self': ma.URLFor('bill_details', values=dict(id='<id>')),
            'collection': ma.URLFor('bills')
        })


bill_schema = BillSchema()
bills_schema = BillSchema(many=True)