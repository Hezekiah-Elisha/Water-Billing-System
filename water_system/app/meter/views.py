from flask import jsonify, request
from . import meter
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
    meters = Meter.get_all_meters()
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
    gps_coordinates = json_data['gps_coordinates']
    customer_id = json_data['customer_id']

    meter = Meter(customer_id=customer_id, meter_number=meter_number, meter_type=meter_type, installation_date=installation_date, gps_coordinates=gps_coordinates)

    meter.save()

    result = meter_schema.dump(meter)

    return jsonify(result), 201


"""
meter reading class routes
"""
@meter.route('/reading', methods=['GET'])
def get_all_meter_readings():
    meter_readings = MeterReading.get_all()
    if not meter_readings:
        return jsonify(message='No meter readings found'), 404
    result = meter_readings_schema.dump(meter_readings)
    return jsonify(result), 200


@meter.route('/reading', methods=['POST'])
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

    meter_reading.save()

    result = meter_reading_schema.dump(meter_reading)

    return jsonify(result=result, message="meter reading added successfull"), 201

    # return jsonify(
    #     meter_id=meter_id,
    #     worker_id=worker_id,
    #     reading_gps_coordinates=reading_gps_coordinates,
    #     meter_status=meter_status,
    #     reading_image_name=name,
    #     reading_date=reading_date,
    #     reading_value=reading_value,
    #     comments=comments
    # ), 201
