from app import db

class Notification(db.Model):
    __tablename__ = 'notifications'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    type = db.Column(db.String, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    message = db.Column(db.String, nullable=False)
    viewed = db.Column(db.Boolean, nullable=False, default=False)
    created_at_time = db.Column(
        db.DateTime,
        nullable=False,
        default=db.func.current_timestamp())

    # Define the one-to-one relationship with Customer
    customer = db.relationship('User', uselist=False, backref='Notification')

    def __init__(self, user_id, type, date, message, viewed):
        self.user_id = user_id
        self.type = type
        self.date = date
        self.message = message
        self.viewed = viewed

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
    

    @staticmethod
    def get_notifications_by_user_id(user_id):
        return Notification.query.filter_by(user_id=user_id).all()
    

    @staticmethod
    def get_notifications_by_type(type):
        return Notification.query.filter_by(type=type).all()
    

    @staticmethod
    def get_notifications_by_date_for_user_id(user_id, date):
        return Notification.query.filter_by(user_id=user_id, date=date).all()
    

    @staticmethod
    def get_notifications_by_user_id_and_views(user_id, viewed):
        return Notification.query.filter_by(user_id=user_id, viewed=viewed).all()
    
