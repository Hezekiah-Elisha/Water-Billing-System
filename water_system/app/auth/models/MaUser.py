from flask_marshmallow import Marshmallow as ma
from flask_marshmallow import fields

from .User import User

ma = ma()


class UserSchema(ma.Schema):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'role', 'created_at')

        _links = ma.Hyperlinks({
            'self': ma.URLFor('user_details', values=dict(id='<id>')),
            'collection': ma.URLFor('users')
        })


user_schema = UserSchema()
users_schema = UserSchema(many=True)
