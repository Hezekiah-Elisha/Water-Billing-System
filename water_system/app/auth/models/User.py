from app import db
import secrets


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=True)
    password = db.Column(db.String, nullable=True)
    email = db.Column(db.String, unique=True, nullable=True)
    role = db.Column(db.String, nullable=True)
    verified = db.Column(db.Boolean, nullable=True, default=False)
    verification_code = db.Column(db.String, nullable=True)
    created_at = db.Column(
        db.DateTime,
        nullable=True,
        default=db.func.current_timestamp())

    def __init__(self, username, password, email, role):
        self.username = username
        self.password = password
        self.email = email
        self.role = role

    def __repr__(self):
        return f'<User {self.username}>'

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return True

    def save(self):
        # check if user exists first
        user = User.query.filter_by(username=self.username).first()
        if user:
            return False
        # generate verification code
        self.verification_code = secrets.token_urlsafe(32)
        db.session.add(self)
        db.session.commit()
        return self

    def update(self):
        db.session.commit()
        return True

    @staticmethod
    def get_all_users():
        return User.query.all()
    

    @staticmethod
    def delete_all_users():
        db.session.query(User).delete()
        db.session.commit()
        return True

    @staticmethod
    def get_user_by_id(id):
        return User.query.get(id)

    @staticmethod
    def get_user_by_username(username):
        return User.query.filter_by(username=username).first()

    @staticmethod
    def get_user_by_email(email):
        return User.query.filter_by(email=email).first()

    @staticmethod
    def get_user_password_by_email(email):
        return User.query.filter_by(email=email).first().password

    # get users with same role
    @staticmethod
    def get_users_by_role(role):
        return User.query.filter_by(role=role).all()

    # get user if paassword matches email
    @staticmethod
    def get_user_by_email_and_password(email, password):
        return User.query.filter_by(email=email, password=password).first()

    # get user if paassword matches username
    @staticmethod
    def get_user_by_username_and_password(username, password):
        return User.query.filter_by(
            username=username,
            password=password).first()

    # verify user
    @staticmethod
    def verify_user(verification_code):
        user = User.query.filter_by(
            verification_code=verification_code).first()
        if not user:
            return False
        user.verified = True
        user.update()
        return True
    
    # return users role when given email
    @staticmethod
    def get_user_role_by_email(email):
        return User.query.filter_by(email=email).first().role


    # return username when given id
    @staticmethod
    def get_user_username_by_id(id):
        return User.query.filter_by(id=id).first().username
    
    @staticmethod
    def get_username(email):
        return User.query.filter_by(email=email).first().username
    
    @staticmethod
    def get_role(email):
        return User.query.filter_by(email=email).first().role