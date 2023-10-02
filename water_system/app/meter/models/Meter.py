from app import db


class Meter(db.Model):
    __tablename__ = 'meters'
    id = db.Column(db.Integer, primary_key=True)
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
        'MeterReading', uselist=False, backref='meter')