from flask import jsonify, request
from . import meter
from flask_jwt_extended import jwt_required
from ..decorators import admin_required, supervisor_required, worker_required
from .models.Meter import Meter
from .models.MaMeter import meter_schema, meters_schema
from .models.MaMeterReading import meter_reading_schema, meter_readings_schema
from .models.MeterReading import MeterReading


@meter.route('/', methods=['GET'])
def get_all_meters():
    meters = Meter.get_all_meters()
    if not meters:
        return jsonify(message='No meters found'), 404
    result = meters_schema.dump(meters)
    return jsonify(result), 200



@meter.route('/', methods=['POST'])
@jwt_required()
@admin_required
def create_meter():
    return jsonify(message='Create meter!')
