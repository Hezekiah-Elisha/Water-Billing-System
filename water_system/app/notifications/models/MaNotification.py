from flask_marshmallow import Marshmallow as ma

from .Notification import Notification


ma = ma()


class NotificationSchema(ma.Schema):
    class Meta:
        model = Notification
        fields = ('id', 'user_id', 'type', 'date', 'message', 'viewed', 'created_at')

        _links = ma.Hyperlinks({
            'self': ma.URLFor('notification_details', values=dict(id='<id>')),
            'collection': ma.URLFor('notifications')
        })
    

notification_schema = NotificationSchema()
notifications_schema = NotificationSchema(many=True)