from app import db
from ...billing.models.Bill import Bill

from datetime import datetime


now = datetime.now()
current_month = now.month
current_year = now.year


def get_previous_date(current_date):
    month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    previous_date = datetime(current_date.year, current_date.month - 1, current_date.day)
    previous_month = current_date.month - 1
    if previous_month == 0:
        previous_month = month[11]
        previous_date = datetime(current_date.year - 1, previous_month, current_date.day)

        return previous_date
    return previous_date

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
        """check if reading exists for the given month as reading_date
        # if exists, don't save
        # if not, save
        """        
        if MeterReading.query.filter_by(reading_date=self.reading_date).first():
            return 'Meter reading already exists for that month'

        if MeterReading.query.filter_by(meter_id=self.meter_id)\
            .filter(db.func.extract('month', MeterReading.reading_date)==self.reading_date.month)\
                .filter(db.func.extract('year', MeterReading.reading_date)==self.reading_date.year).first():
            return 'Meter reading already exists for that month 2'


        db.session.add(self)

        # calculate bill
        if MeterReading.calculate_bill(self.meter_id, self.reading_date.month, self.reading_date.year):
            db.session.commit()
            return "Meter reading added successfully"
        return "Meter reading added successfully but bill not calculated"


    
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
    

    # get meterreading by meter id given this month
    @staticmethod
    def get_by_meter_id_given_month(meter_id, month, year):
        return MeterReading.query.filter_by(meter_id=meter_id)\
            .filter(db.func.extract('month', MeterReading.reading_date)==month)\
                .filter(db.func.extract('year', MeterReading.reading_date)==year).all()
    

    @staticmethod
    def get_reading_value_given_month(meter_id, month, year):
        info = MeterReading.query.filter_by(meter_id=meter_id)\
            .filter(db.func.extract('month', MeterReading.reading_date)==month)\
                .filter(db.func.extract('year', MeterReading.reading_date)==year).first()
        
        info.reading_value = float(info.reading_value)

        return info.reading_value
    
    
    @staticmethod
    def get_reading_units_given_month(meter_id, month, year):
        given_date = datetime(year, month, 1)
        current_month = MeterReading.query.filter_by(meter_id=meter_id)\
            .filter(db.func.extract('month', MeterReading.reading_date)==given_date.month)\
                .filter(db.func.extract('year', MeterReading.reading_date)==given_date.year).first()
        if not current_month:
            return 'No meter readings found on that month'

        previous_date = get_previous_date(given_date)

        previous_month = MeterReading.query.filter_by(meter_id=meter_id)\
            .filter(db.func.extract('month', MeterReading.reading_date)==previous_date.month)\
                .filter(db.func.extract('year', MeterReading.reading_date)==previous_date.year).first()
        
        if not previous_month:
            return 'No meter readings found on previous month of that'
        
        current_month.reading_value = float(current_month.reading_value)
        previous_month.reading_value = float(previous_month.reading_value)

        return current_month.reading_value - previous_month.reading_value
    
    @staticmethod
    def calculate_bill(meter_id, month, year):
        given_date = datetime(year, month, 1)

        units = MeterReading.get_reading_units_given_month(meter_id, month, year)

        bill = Bill(meter_id, units, 'unpaid')
        bill.save()
        return True