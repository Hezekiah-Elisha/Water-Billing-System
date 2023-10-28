from app import db


class Supervisor(db.Model):
    __tablename__ = 'supervisors'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    phone = db.Column(db.String, nullable=False, unique=True)
    location = db.Column(db.String, nullable=False)
    created_at = db.Column(
        db.DateTime,
        nullable=True,
        default=db.func.current_timestamp())
    

    # create a one to many relationship with the workers table
    workers = db.relationship('Worker', backref='Supervisor', lazy=True)

    def __init__(self, user_id, phone, location):
        self.user_id= user_id
        self.phone = phone
        self.location = location


    def __repr__(self):
        return f'<Supervisor {self.phone}>'
    

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return True
    

    def save(self):
        # check if phone and email are unique
        supervisor = Supervisor.query.filter_by(phone=self.phone).first()
        if supervisor:
            return False
        supervisor = Supervisor.query.filter_by(id=self.id).first()
        if supervisor:
            return False
        supervisor = Supervisor.query.filter_by(user_id=self.user_id).first()
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
    def get_supervisor_by_location(location):
        return Supervisor.query.filter_by(location=location).first()
            

    @staticmethod
    def get_supervisor_by_user_id(user_id):
        return Supervisor.query.filter_by(user_id=user_id).first()

