from enum import Enum
import sqlalchemy
from . import db


class ItemType(Enum):
    MACHINERY = 1
    TOOLS = 2
    LIVESTOCK = 3
    PRODUCE = 4

    def __str__(self):
        return self.name


class Item(db.Model):
    __tablename__ = 'item'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(100), nullable=True)
    item_type = db.Column(sqlalchemy.types.Enum(ItemType), nullable=True)
    posting_id = db.Column(db.Integer, db.ForeignKey('posting.id'), nullable=False)

    def __init__(self, name, price, description, item_type, posting_id):
        self.name = name
        self.price = price
        self.description = description
        self.item_type = ItemType(item_type)
        self.posting_id = posting_id

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'item_type': self.item_type.__str__(),
            'posting_id': self.posting_id
        }


class Posting(db.Model):
    __tablename__ = 'posting'
    id = db.Column(db.Integer, primary_key=True)
    posting_item = db.relationship('Item', uselist=False, lazy=True)
    posting_status = db.Column(db.String(15), default='Processing')
    in_stock = db.Column(db.Integer, nullable=False, default=0)
    user_id = db.Column(db.Integer, nullable=False)

    def __init__(self, user_id):
        self.user_id = user_id

    def serialize(self):
        return {
            'id': self.id,
            'posting_item': self.posting_item.serialize(),
            'posting_status': self.posting_status,
            'in_stock': self.in_stock,
            'user_id': self.user_id
        }
