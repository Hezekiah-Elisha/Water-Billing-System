from flask import jsonify, request
from . import notification
from .models.Notification import Notification
from .models.MaNotification import notification_schema, notifications_schema
from datetime import datetime

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


@notification.route('/', methods=['POST'])
def create():
    req_data = request.get_json()
    if not req_data:
        return jsonify(message='No input data provided'), 400
    
    user_id = req_data['user_id']
    notification_type = req_data['type']
    notification_date = datetime.strptime(req_data['date'], '%Y-%m-%d %H:%M:%S')
    notification_message = req_data['message']
    notification_viewed = req_data['viewed']

    notification = Notification(user_id, notification_type, notification_date, notification_message, viewed=notification_viewed)
    notification.save()
    result = notification_schema.dump(notification)
    return jsonify(result), 201