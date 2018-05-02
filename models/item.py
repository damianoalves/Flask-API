from db import db


# item model
class ItemModel(db.Model):

    # items table configuration
    __tablename__ = 'items'
    nome = db.Column(db.String(100), primary_key=True)
    description = db.Column(db.String(100))
    traduction = db.Column(db.String(100))

    # constructor
    def __init__(self, nome, description, traduction):
        self.nome = nome
        self.description = description
        self.traduction = traduction

    # this method will parse and convert a Item object to json format
    def json(self):
        return {'item': {'name': self.nome,
                         'description': self.description,
                         'traduction': self.traduction}}

    # find a item by his name
    @classmethod
    def find_by_name(cls, nome):
        return cls.query.filter_by(nome=nome).first()

    # save a item into db
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    # delete a item from the db
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
