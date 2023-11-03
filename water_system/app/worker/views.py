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


@worker.route('/workers/<int:worker_id>', methods=['GET'])
def get_worker(worker_id):
    worker = Worker.get_worker_by_id(worker_id)
    if not worker:
        return jsonify(message='Worker not found'), 404
    result = worker_schema.dump(worker)
    return jsonify(result), 200