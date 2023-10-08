from flask import jsonify, request
from . import notification
from .models.Notification import Notification
from .models.MaNotification import notification_schema, notifications_schema

@notification.route('/', methods=['GET'])
def get_all_notifications():
    notifications = Notification.get_all_notifications()
    if not notifications:
        return jsonify(message='No notifications found'), 404
    result = notifications_schema.dump(notifications)
    return jsonify(result), 200

    
@notification.route('/test', methods=['GET'])
def test():
    return jsonify(message='Notification endpoint working'), 200
