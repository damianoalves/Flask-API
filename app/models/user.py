from sqlalchemy import Integer, String

from app import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(Integer, primary_key=True)
    fullname = db.Column(String(50), nullable=False)
    nickname = db.Column(String(20), nullable=False, unique=True)
    password = db.Column(String(20), nullable=False)

    def __init__(self, fullname, nickname, password):
        self.fullname = fullname
        self.nickname = nickname
        self.password = password

    def __repr__(self):
        return "<User(fullname='%s', nickname='%s')>" % (self.fullname, self.nickname)
