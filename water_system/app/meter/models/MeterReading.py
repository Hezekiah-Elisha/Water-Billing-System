from app import db


class MeterReading(db.Model):
    __tablename__ = 'meter_readings'
    id = db.Column(db.Integer, primary_key=True)
    meter_id = db.Column(
        db.Integer,
        db.ForeignKey('meters.id'),
        nullable=False)
    worker_id = db.Column(
        db.Integer,
        db.ForeignKey('workers.id'),
        nullable=False)
    reading_gps_coordinates = db.Column(db.String, nullable=False)
    meter_status = db.Column(db.String, nullable=False)
    reading_image = db.Column(db.String, nullable=False)
    reading_date = db.Column(db.DateTime, nullable=False)
    reading_value = db.Column(db.Float, nullable=False)
    comments = db.Column(db.Text, nullable=True)
    created_at = db.Column(
        db.DateTime,
        nullable=True,
        default=db.func.current_timestamp())

    # Define the one-to-one relationship with Meter
    # meter = db.relationship('Meter', uselist=False, backref='MeterReading')
    # Define the one-to-one relationship with Worker
    worker = db.relationship('Worker', backref='MeterReading')

    def __repr__(self):
        return '<MeterReading {}>'.format(self.id)
    
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
        return MeterReading.query.all()
    
    @staticmethod
    def get_by_id(id):
        return MeterReading.query.get(id)
    
    @staticmethod
    def get_by_meter_id(meter_id):
        return MeterReading.query.filter_by(meter_id=meter_id).all()