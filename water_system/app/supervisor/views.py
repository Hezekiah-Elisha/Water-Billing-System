from flask import jsonify, request
from . import supervisor
from .models.Supervisor import Supervisor
from .models.MaSupervisor import supervisor_schema, supervisors_schema
# from .forms import SupervisorForm

@supervisor.route('/', methods=['GET'])
def get_all_supervisors():
    supervisors = Supervisor.get_all_supervisors()
    if not supervisors:
        return jsonify(message='No supervisors found'), 404
    result = supervisors_schema.dump(supervisors)
    return jsonify(result), 200

@supervisor.route('/test', methods=['GET'])
def test():
    return jsonify(message='Supervisor endpoint working'), 200

@supervisor.route('/', methods=['POST'])
def create_supervisor():
    user_id = request.json.get('user_id', None)
    phone = request.json.get('phone', None)
    location = request.json.get('location', None)

    if not user_id:
        return jsonify(message='User ID is required'), 400
    if not phone:
        return jsonify(message='Phone is required'), 400
    if not location:
        return jsonify(message='Location is required'), 400
        
    supervisor = Supervisor(user_id=user_id, phone=phone, location=location)
    info = supervisor.save()

    if not info:
        return jsonify(message='Supervisor already exists'), 409
    
    supervisor_info = supervisor_schema.dump(info)
    
    return jsonify(message='Supervisor created successfully', supervisor=supervisor_info), 201


@supervisor.route('/<int:user_id>', methods=['GET'])
def get_supervisor(user_id):
    supervisor = Supervisor.get_supervisor_by_user_id(user_id)
    if not supervisor:
        return jsonify(message='Supervisor not found', isThere=False), 404
    result = supervisor_schema.dump(supervisor)
    return jsonify(supervisor=result, isThere=True), 200