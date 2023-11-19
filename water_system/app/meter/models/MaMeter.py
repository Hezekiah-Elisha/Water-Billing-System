from flask_marshmallow import Marshmallow as ma

from .Meter import Meter

ma = ma()


class MeterSchema(ma.Schema):
    class Meta:
        model = Meter
        fields = ('id', 'customer_id', 'meter_number', 'meter_type', 'installation_date', 'gps_coordinates', 'created_at')

        _links = ma.Hyperlinks({
            'self': ma.URLFor('meter_details', values=dict(id='<id>')),
            'collection': ma.URLFor('meters')
        })


meter_schema = MeterSchema()
meters_schema = MeterSchema(many=True)