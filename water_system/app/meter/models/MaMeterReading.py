from flask_marshmallow import Marshmallow as ma

from .MeterReading import MeterReading

ma = ma()


class MeterReadingSchema(ma.Schema):
    class Meta:
        model = MeterReading
        fields = ('id', 'meter_id', 'reading', 'created_at')

        _links = ma.Hyperlinks({
            'self': ma.URLFor('meter_reading_details', values=dict(id='<id>')),
            'collection': ma.URLFor('meter_readings')
        })


meter_reading_schema = MeterReadingSchema()
meter_readings_schema = MeterReadingSchema(many=True)