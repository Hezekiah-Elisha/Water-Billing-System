from flask import jsonify, request
from . import supervisor
from .models.Supervisor import Supervisor
from .models.MaSupervisor import supervisor_schema, supervisors_schema

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