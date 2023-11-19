from flask import jsonify, request, send_from_directory
from . import meter, readings
from flask_jwt_extended import jwt_required
from ..decorators import admin_required, supervisor_required, worker_required
from .models.Meter import Meter
from .models.MaMeter import meter_schema, meters_schema
from .models.MaMeterReading import meter_reading_schema, meter_readings_schema
from .models.MeterReading import MeterReading
from datetime import datetime, timedelta, timezone
import os
from werkzeug.utils import secure_filename
from werkzeug.exceptions import RequestEntityTooLarge
from ..billing.models.Bill import Bill


now = datetime.now()
current_month = now.month
current_year = now.year

MAX_CONTENT_LENGTH = 4 * 1024 * 1024

allowed_extensions = {'jpg', 'png'}

# UPLOAD_FOLDER = '/home/hezekiah/Desktop/work/4th year project/water_system/app/meter/uploads'
basedir = os.path.abspath(os.path.dirname(__file__))
upload_folder = os.path.join(basedir, 'uploads')


@meter.route('/test', methods=['GET'])
def test():
    return jsonify(dir=upload_folder), 200

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in allowed_extensions


def upload_image(image):
    if image and allowed_file(image.filename):
        filename = secure_filename(image.filename)
        image.save(os.path.join(upload_folder, filename))
        return filename


""" 

meter class routes

"""
@meter.route('/', methods=['GET'])
def get_all_meters():
    meters = Meter.get_all()
    if not meters:
        return jsonify(message='No meters found'), 404
    result = meters_schema.dump(meters)
    return jsonify(result), 200


@meter.route('/', methods=['POST'])
def create_meter():
    json_data = request.get_json()
    if not json_data:
        return jsonify(message='No input data provided'), 400
    # Validate and deserialize input
    # data = meter_schema.load(json_data)
    # meter = Meter(data)
    # meter.save()
    # result = meter_schema.dump(meter)

    meter_number = json_data['meter_number']
    meter_type = json_data['meter_type']
    installation_date = datetime.strptime(json_data['installation_date'], '%Y-%m-%d %H:%M:%S')
    # installation_date = json_data['installation_date']
    gps_coordinates = json_data['gps_coordinates']
    customer_id = json_data['customer_id']

    meter = Meter(customer_id=customer_id, meter_number=meter_number, meter_type=meter_type, installation_date=installation_date, gps_coordinates=gps_coordinates)

    meter.save()
    
    meters = Meter.get_all()
    if not meters:
        return jsonify(message='No meters found'), 404
    result = meters_schema.dump(meters)


    return jsonify(result), 201


@meter.route('/<int:meter_id>', methods=['GET'])
def get_meter_by_id(meter_id):
    meter = Meter.get_by_id(meter_id)
    if not meter:
        return jsonify(message='No meter found'), 404
    result = meter_schema.dump(meter)
    return jsonify(result), 200


"""
meter reading class routes
"""
@readings.route('/', methods=['GET'])
def get_all_meter_readings():
    meter_readings = MeterReading.get_all()
    if not meter_readings:
        return jsonify(message='No meter readings found'), 404
    result = meter_readings_schema.dump(meter_readings)
    return jsonify(result), 200


@readings.route('/', methods=['POST'])
def create_meter_reading():
    meter_id = request.form['meter_id']
    worker_id = request.form['worker_id']
    reading_gps_coordinates = request.form['reading_gps_coordinates']
    meter_status = request.form['meter_status']
    reading_image = request.files['reading_image']
    reading_date = datetime.strptime(request.form['reading_date'], '%Y-%m-%d %H:%M:%S')
    reading_value = request.form['reading_value']
    comments = request.form['comments']

    if reading_image.filename == '':
        return jsonify(message='No image provided'), 400
    
    if reading_image and allowed_file(reading_image.filename):
        name = upload_image(reading_image)

    meter_reading = MeterReading(
        meter_id=meter_id,
        worker_id=worker_id,
        reading_gps_coordinates=reading_gps_coordinates,
        meter_status=meter_status,
        reading_image=name,
        reading_date=reading_date,
        reading_value=reading_value,
        comments=comments
    )

    info = meter_reading.save()

    meter_reading_ish = MeterReading.get_month_and_year(reading_date)

    units = MeterReading.get_reading_units_given_month(meter_id, meter_reading_ish[0], meter_reading_ish[1])
    
    billing = Bill(meter_id=meter_id, units=units, status='unpaid')

    billing.save()

    # result = meter_reading_schema.dump(meter_reading)

    return jsonify(result=info), 201


# delete all meter readings
@readings.route('/', methods=['DELETE'])
def delete_all_meter_readings():
    meter_readings = MeterReading.get_all()
    if not meter_readings:
        return jsonify(message='No meter readings found'), 404
    for meter_reading in meter_readings:
        meter_reading.delete()

    readings = MeterReading.get_all()
    if readings:
        return jsonify(message='Failed to delete all meter readings'), 500

    return jsonify(message='All meter readings deleted', readings=readings), 200


@readings.route('/<int:meter_id>', methods=['GET'])
def get_meter_readings(meter_id):
    meter_readings = MeterReading.get_by_meter_id(meter_id)
    if not meter_readings:
        return jsonify(message='No meter readings found'), 404
    result = meter_readings_schema.dump(meter_readings)
    return jsonify(result), 200


@readings.route('/<int:meter_id>/<int:year>/<int:month>', methods=['GET'])
def get_meter_readings_by_month(meter_id, year, month):
    meter_readings = MeterReading.get_by_meter_id_this_month(meter_id, month, year)
    if not meter_readings:
        return jsonify(message='No meter readings found'), 404
    result = meter_readings_schema.dump(meter_readings)
    return jsonify(result), 200


@readings.route('/reading_value/<int:meter_id>/<int:year>/<int:month>', methods=['GET'])
def get_meter_reading_value(meter_id, year, month):
    meter_readings = MeterReading.get_reading_value_given_month(meter_id, month, year)
    if not meter_readings:
        return jsonify(message='No meter readings found'), 404

    return jsonify(reading_value=meter_readings), 200



@readings.route('/units/<int:meter_id>/<int:year>/<int:month>', methods=['GET'])
def units(meter_id, year, month):
    units = MeterReading.get_reading_units_given_month(meter_id, month, year)
    if not units:
        return jsonify(message='No meter readings found'), 404
    return jsonify(units=units), 200


@readings.route('uploads/<filename>', methods=['GET'])
def uploaded_file(filename):
    return send_from_directory(upload_folder, filename)
