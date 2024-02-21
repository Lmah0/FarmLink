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
    posting_status = db.Column(db.String(15), default='Processing')
    user_id = db.Column(db.Integer, nullable=False)

    def __init__(self, name, price, description, item_type, user_id):
        self.name = name
        self.price = price
        self.description = description
        self.item_type = ItemType(item_type)
        self.user_id = user_id

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'item_type': self.item_type.__str__(),
            'user_id': self.user_id
        }
