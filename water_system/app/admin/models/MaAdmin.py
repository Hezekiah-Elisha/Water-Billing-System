from flask_marshmallow import Marshmallow as ma
from .Admin import Admin

ma = ma()


class AdminSchema(ma.Schema):
    class Meta:
        model = Admin
        fields = ('id', 'name', 'email', 'phone', 'created_at')

        _links = ma.Hyperlinks({
            'self': ma.URLFor('admin_details', values=dict(id='<id>')),
            'collection': ma.URLFor('admins')
        })
    

admin_schema = AdminSchema()
admins_schema = AdminSchema(many=True)