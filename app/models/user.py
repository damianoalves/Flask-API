from flask_restful.fields import Integer, String
from app import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(Integer, primary_key=True)
    name = db.Column(String)
    fullname = db.Column(String)
    nickname = db.Column(String)

    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (self.name, self.fullname, self.nickname)
