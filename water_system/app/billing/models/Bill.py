from app import db


class Bill(db.Model):
    __tablename__ = 'bills'
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    amount = db.Column(db.Integer, nullable=True)
    status = db.Column(db.String, nullable=True)
    created_at = db.Column(
        db.DateTime,
        nullable=True,
        default=db.func.current_timestamp())
    

    def __init__(self, customer_id, amount, status):
        self.customer_id = customer_id
        self.amount = amount
        self.status = status

    
    def __repr__(self):
        return f'<Bill {self.id}>'
    

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
    def get_all_bills():
        return Bill.query.all()
    

    @staticmethod
    def get_bill_by_id(id):
        return Bill.query.get(id)
    

    @staticmethod
    def get_bill_by_customer_id(customer_id):
        return Bill.query.filter_by(customer_id=customer_id).first()