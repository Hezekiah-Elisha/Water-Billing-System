from app import db


class Worker(db.Model):
    __tablename__ = 'workers'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    supervisor_id = db.Column(db.Integer, db.ForeignKey('supervisors.id'))
    name = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    location = db.Column(db.String, nullable=False)
    created_at = db.Column(
        db.DateTime,
        nullable=True,
        default=db.func.current_timestamp())
    

    def __init__(self, user_id, supervisor_id, name, phone, email, location):
        self.user = user_id
        self.supervisor = supervisor_id
        self.name = name
        self.phone = phone
        self.email = email
        self.location = location


    def __repr__(self):
        return f'<Worker {self.name}>'
    

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return True
    

    def save(self):
        # check if phone and email are unique
        worker = Worker.query.filter_by(phone=self.phone).first()
        if worker:
            return False
        worker = Worker.query.filter_by(email=self.email).first()
        if worker:
            return False
        db.session.add(self)
        db.session.commit()
        return self
    

    def update(self):
        db.session.commit()
        return True
    

    @staticmethod
    def get_all_workers():
        return Worker.query.all()
    

    @staticmethod
    def get_worker_by_id(id):
        return Worker.query.get(id)
    
    
    # get workers with same supervisor
    @staticmethod
    def get_workers_by_supervisor(supervisor_id):
        return Worker.query.filter_by(supervisor_id=supervisor_id).all()


    # get workers by email
    @staticmethod
    def get_worker_by_email(email):
        return Worker.query.filter_by(email=email).first()        
