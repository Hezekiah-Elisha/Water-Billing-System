from app import db


class MeterReading(db.Model):
    __tablename__ = 'meter_readings'
    id = db.Column(db.Integer, primary_key=True)
    meter_id = db.Column(
        db.Integer,
        db.ForeignKey('meters.id'),
        nullable=False)
    reading_gps_coordinates = db.Column(db.String, nullable=False)
    meter_status = db.Column(db.String, nullable=False)
    reading_date = db.Column(db.DateTime, nullable=False)
    reading_value = db.Column(db.Float, nullable=False)
    comments = db.Column(db.String, nullable=True)
    created_at = db.Column(
        db.DateTime,
        nullable=True,
        default=db.func.current_timestamp())

    # Define the one-to-one relationship with Meter
    meter = db.relationship('Meter', uselist=False, backref='meter_reading')