from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from db import db
from models.item import ItemModel


class Item(Resource):

    # this parser will going to require name, description and traduction for any item that will be created
    parser = reqparse.RequestParser()
    parser.add_argument('description',
                        type=str,
                        required=True,
                        help="This argument cannot be blank.")
    parser.add_argument('traduction',
                        type=str,
                        required=True,
                        help="This argument cannot be blank.")

    # get method to return a item
    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404

    # post method to create a item
    @jwt_required()
    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message': "The item named '{}' already exists.".format(name)}, 400
        data = Item.parser.parse_args()
        item = ItemModel(name, data['description'], data['traduction'])
        item.save_to_db()
        return data, 201

    # delete method to remove a item from the list
    @jwt_required()
    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            db.session.delete(item)
            db.session.commit()
            return {'message': 'Item deleted'}, 200
        return {'message': "The item named '{}' do not exists.".format(name)}, 404

    # put method to update a item
    @jwt_required()
    def put(self, name):
        item = ItemModel.find_by_name(name)
        if item is None:
            return {'message': "The item named '{}' do not exists.".format(name)}, 404
        data = Item.parser.parse_args()
        item.description = data['description']
        item.traduction = data['traduction']
        item.save_to_db()
        return item.json(), 200


class ItemList(Resource):
    # get method to return the complete items list
    @jwt_required()
    def get(self):
        return {'items': [item.json() for item in ItemModel.query.all()]}
