from app import db


class Meter(db.Model):
    __tablename__ = 'meters'
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    meter_number = db.Column(db.String, unique=True, nullable=False)
    meter_type = db.Column(db.String, nullable=False)
    installation_date = db.Column(db.DateTime, nullable=False)
    gps_coordinates = db.Column(db.String, nullable=False)
    created_at = db.Column(
        db.DateTime,
        nullable=True,
        default=db.func.current_timestamp())
    

    # Define the one-to-one relationship with MeterReading
    meter_reading = db.relationship(
        'MeterReading', uselist=False, backref='Meter')
    # Define the one-to-one relationship with Customer
    customer = db.relationship('Customer', uselist=False, backref='Meter')

    def __repr__(self):
        return '<Meter {}>'.format(self.id)
    
    def save(self):
        db.session.add(self)
        db.session.commit()
        return self.id
    
    def update(self):
        db.session.commit()
        return self.id
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return self.id
    

    @staticmethod
    def get_all():
        return Meter.query.all()
    
    @staticmethod
    def get_by_id(id):
        return Meter.query.get(id)
    
    @staticmethod
    def get_by_customer_id(customer_id):
        return Meter.query.filter_by(customer_id=customer_id).all()