from app import db


class TokenBlocklist(db.Model):
    __tablename__ = 'token_blocklist'
    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(36), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    def __init__(self, jti, created_at):
        self.jti = jti
        self.created_at = created_at

    def save(self):
        db.session.add(self)
        db.session.commit()
        return True

    # get token by id filter by jti
    @staticmethod
    def get_token_by_id(jti):
        token = db.session.query(TokenBlocklist.id).filter_by(jti=jti).scalar()

        return token
