from . import worker
from flask import jsonify, request
from .models.Worker import Worker
from .models.MaWorker import worker_schema, workers_schema

@worker.route('/workers', methods=['GET'])
def get_all_workers():
    workers = Worker.get_all_workers()
    if not workers:
        return jsonify(message='No workers found'), 404
    result = workers_schema.dump(workers)
    return jsonify(result), 200

@worker.route('/test', methods=['GET'])
def test():
    return jsonify(message='Worker endpoint working'), 200