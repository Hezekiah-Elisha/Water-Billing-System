from app import db

class Notification(db.Model):
    __tablename__ = 'notifications'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    notification_type = db.Column(db.String, nullable=False)
    notification_date = db.Column(db.DateTime, nullable=False)
    notification_message = db.Column(db.String, nullable=False)
    created_at = db.Column(
        db.DateTime,
        nullable=True,
        default=db.func.current_timestamp())

    # Define the one-to-one relationship with Customer
    customer = db.relationship('User', uselist=False, backref='Notification')

    def __init__(self, user_id, notification_type, notification_date, notification_message):
        self.user_id = user_id
        self.notification_type = notification_type
        self.notification_date = notification_date
        self.notification_message = notification_message

    def __repr__(self):
        return f'<Notification {self.id}>'


    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return True
    

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self
    

    def update(self):
        db.session.commit()
        return True
    

    @staticmethod
    def get_all_notifications():
        return Notification.query.all()
    

    @staticmethod
    def get_notification_by_id(id):
        return Notification.query.get(id)
    
