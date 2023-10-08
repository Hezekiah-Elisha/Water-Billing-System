from flask_marshmallow import Marshmallow as ma
from .Worker import Worker

ma = ma()


class WorkerSchema(ma.Schema):
    class Meta:
        model = Worker
        fields = ('id', 'name', 'email', 'phone', 'created_at')

        _links = ma.Hyperlinks({
            'self': ma.URLFor('worker_details', values=dict(id='<id>')),
            'collection': ma.URLFor('workers')
        })


worker_schema = WorkerSchema()
workers_schema = WorkerSchema(many=True)