from db import db


# user class
class User(db.Model):

    # user table configuration
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))

    # constructor
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    # this method will look in the db the user based on his username
    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    # this method will look in the db the user based on his id
    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    # this method will save a user in the db
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()