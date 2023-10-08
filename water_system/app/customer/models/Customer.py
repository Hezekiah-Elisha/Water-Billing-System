from app import db


class Customer(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    phone = db.Column(db.String, nullable=True, unique=True)
    email = db.Column(db.String, nullable=True, unique=True)
    location = db.Column(db.String, nullable=True)
    created_at = db.Column(
        db.DateTime,
        nullable=True,
        default=db.func.current_timestamp())
    
    # Define the one-to-one relationship with Meter
    meter = db.relationship('Meter', uselist=False, backref='Customer')

    def __init__(self, name, phone, email, location):
        self.name = name
        self.phone = phone
        self.email = email
        self.location = location

    
    def __repr__(self):
        return f'<Customer {self.name}>'
    

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return True
    

    def save(self):
        # check if phone and email are unique
        customer = Customer.query.filter_by(phone=self.phone).first()
        if customer:
            return False
        customer = Customer.query.filter_by(email=self.email).first()
        if customer:
            return False
        db.session.add(self)
        db.session.commit()
        return self
    

    def update(self):
        db.session.commit()
        return True
    

    @staticmethod
    def get_all_customers():
        return Customer.query.all()
    

    @staticmethod
    def get_customer_by_id(id):
        return Customer.query.get(id)
    

    @staticmethod
    def get_customer_by_phone(phone):
        return Customer.query.filter_by(phone=phone).first()
    
    @staticmethod
    def get_customer_by_email(email):
        return Customer.query.filter_by(email=email).first()
    
    @staticmethod
    def get_customer_by_name(name):
        return Customer.query.filter_by(name=name).first()


    @staticmethod
    def get_customer_by_location(location):
        return Customer.query.filter_by(location=location).first()
    
    # get customers by location
    @staticmethod
    def get_customers_by_location(location):
        return Customer.query.filter_by(location=location).all()
    
    # get customers by almost similar names
    @staticmethod
    def get_customers_by_name(name):
        return Customer.query.filter(Customer.name.like('%'+name+'%')).all()
    

    # get customers by almost similar phone numbers
    @staticmethod
    def get_customers_by_phone(phone):
        return Customer.query.filter(Customer.phone.like('%'+phone+'%')).all()
    