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

    notification = Notification(user_id, type=notification_type, date=notification_date, message=notification_message, viewed=notification_viewed)
    notification.save()
    # result = notification_schema.dump(notification)

    all_notifications = Notification.get_all_notifications()
    all_notifications = notifications_schema.dump(all_notifications)

    return jsonify(message="Notification Sent", result=all_notifications), 201


@notification.route('/<int:id>', methods=['GET'])
def get_notification(id):
    notification = Notification.get_notification_by_id(id)
    if not notification:
        return jsonify(message='Notification not found'), 404
    result = notification_schema.dump(notification)
    return jsonify(result), 200


@notification.route('/<int:id>', methods=['PUT'])
def update_notification(id):
    req_data = request.get_json()
    notification = Notification.get_notification_by_id(id)
    if not notification:
        return jsonify(message='Notification not found'), 404
    if not req_data:
        return jsonify(message='No input data provided'), 400
    
    notification.user_id = req_data['user_id']
    notification.type = req_data['type']
    notification.date = datetime.strptime(req_data['date'], '%Y-%m-%d %H:%M:%S')
    notification.message = req_data['message']
    notification.viewed = req_data['viewed']
    notification.update()
    result = notification_schema.dump(notification)
    return jsonify(result), 200


@notification.route('/<int:id>', methods=['DELETE'])
def delete_notification(id):
    notification = Notification.get_notification_by_id(id)
    if not notification:
        return jsonify(message='Notification not found'), 404
    notification.delete()
    return jsonify(message='Notification deleted'), 200