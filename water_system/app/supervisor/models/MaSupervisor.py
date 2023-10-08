from flask_marshmallow import Marshmallow as ma

from .Supervisor import Supervisor


ma = ma()


class SupervisorSchema(ma.Schema):
    class Meta:
        model = Supervisor
        fields = ('id', 'name', 'email', 'phone', 'created_at')

        _links = ma.Hyperlinks({
            'self': ma.URLFor('supervisor_details', values=dict(id='<id>')),
            'collection': ma.URLFor('supervisors')
        })


supervisor_schema = SupervisorSchema()
supervisors_schema = SupervisorSchema(many=True)