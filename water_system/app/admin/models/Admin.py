from app import db


class Admin(db.Model):
    __tablename__ = 'admins'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    phone = db.Column(db.String, nullable=True, unique=True)
    email = db.Column(db.String, nullable=True, unique=True)
    location = db.Column(db.String, nullable=True)
    password = db.Column(db.String, nullable=True)
    created_at = db.Column(
        db.DateTime,
        nullable=True,
        default=db.func.current_timestamp())
    

    def __init__(self, name, phone, email, location, password):
        self.name = name
        self.phone = phone
        self.email = email
        self.location = location
        self.password = password

    
    def __repr__(self):
        return f'<Admin {self.name}>'
    

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return True
    

    def save(self):
        # check if phone and email are unique
        admin = Admin.query.filter_by(phone=self.phone).first()
        if admin:
            return False
        admin = Admin.query.filter_by(email=self.email).first()
        if admin:
            return False
        db.session.add(self)
        db.session.commit()
        return self
    

    def update(self):
        db.session.commit()
        return True
    

    @staticmethod
    def get_all_admins():
        return Admin.query.all()
    

    @staticmethod
    def get_admin_by_id(id):
        return Admin.query.get(id)
