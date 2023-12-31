from webapp import db
from flask_login import UserMixin
from passlib.hash import pbkdf2_sha256 as sha256

class UserModel(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(120), unique = True, nullable = False)
    password = db.Column(db.String(120), nullable = False)
    secret = db.Column(db.Integer, nullable = False)
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username = username).first()
        
    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id = id).first()

    @classmethod
    def delete_all(cls):
        try:
            num_rows_deleted = db.session.query(cls).delete()
            db.session.commit()
            return {'message': '{} row(s) deleted'.format(num_rows_deleted)}
        except:
            return {'message': 'Something went wrong'}

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)
    @staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password, hash)


class CommentsModel(db.Model):
    __tablename__ = 'comments'
    
    id = db.Column(db.Integer, primary_key = True)
    text = db.Column(db.String(255))
    
    def add(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def getAll(cls):
        query = cls.query.all()
        return query

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()