from app import db


class Supervisor(db.Model):
    __tablename__ = 'supervisors'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    name = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    location = db.Column(db.String, nullable=False)
    created_at = db.Column(
        db.DateTime,
        nullable=True,
        default=db.func.current_timestamp())
    

    # create a one to many relationship with the workers table
    workers = db.relationship('Worker', backref='Supervisor', lazy=True)

    def __init__(self, user_id, name, phone, email, location):
        self.user = user_id
        self.name = name
        self.phone = phone
        self.email = email
        self.location = location


    def __repr__(self):
        return f'<Supervisor {self.name}>'
    

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return True
    

    def save(self):
        # check if phone and email are unique
        supervisor = Supervisor.query.filter_by(phone=self.phone).first()
        if supervisor:
            return False
        supervisor = Supervisor.query.filter_by(email=self.email).first()
        if supervisor:
            return False
        db.session.add(self)
        db.session.commit()
        return self


    def update(self):
        db.session.commit()
        return True
    

    @staticmethod
    def get_all_supervisors():
        return Supervisor.query.all()
    

    @staticmethod
    def get_supervisor_by_id(id):
        return Supervisor.query.get(id)
    

    @staticmethod
    def get_supervisor_by_phone(phone):
        return Supervisor.query.filter_by(phone=phone).first()
    
    @staticmethod
    def get_supervisor_by_email(email):
        return Supervisor.query.filter_by(email=email).first()
    
    
    @staticmethod
    def get_supervisor_by_name(name):
        return Supervisor.query.filter_by(name=name).first()
    
    @staticmethod
    def get_supervisor_by_location(location):
        return Supervisor.query.filter_by(location=location).first()
            
