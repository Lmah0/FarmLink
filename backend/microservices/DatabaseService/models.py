from enum import Enum

import sqlalchemy

from server import db
from server import app


class TestModel(db.Model):
    __tablename__ = 'test_model'
    id = db.Column(db.Integer, primary_key=True)
    entry = db.Column(db.String(100), unique=True)

    def __init__(self, entry):
        self.entry = entry


class CreditCard(db.Model):
    __tablename__ = 'credit_card'
    id = db.Column(db.Integer, primary_key=True)
    card_number = db.Column(db.String(16), unique=True)
    expiration_date = db.Column(db.DateTime, nullable=False)
    cvv = db.Column(db.String(3))

    def __init__(self, cardNumber, expirationDate, cvv):
        self.card_number = cardNumber
        self.expiration_date = expirationDate
        self.cvv = cvv


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
    name = db.Column(db.String(100))
    price = db.Column(db.Float)
    description = db.Column(db.String(100))
    item_type = db.Column(sqlalchemy.types.Enum(ItemType))

    def __init__(self, name, price, description, itemType):
        self.name = name
        self.price = price
        self.description = description
        self.item_type = itemType


order_items = db.Table('order_items',
                       db.Column('order_id', db.Integer, db.ForeignKey('order.id')),
                       db.Column('item_id', db.Integer, db.ForeignKey('item.id'))
                       )


class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True)
    purchase_date = db.Column(db.DateTime, nullable=False)
    total_cost = db.Column(db.Float, nullable=False)
    order_status = db.Column(db.String(15), default='Processing')
    items = db.relationship('Item', secondary=order_items)

    def __init__(self, purchaseDate, totalCost):
        self.purchase_date = purchaseDate
        self.total_cost = totalCost


class Posting(db.Model):
    __tablename__ = 'posting'
    id = db.Column(db.Integer, primary_key=True)
    posting_item = db.relationship('Item', uselist=False, lazy=True)
    posting_status = db.Column(db.String(15), default='Processing')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, postingStatus):
        self.__postingStatus = postingStatus


class Role(Enum):
    FARMER = 0
    NONFARMER = 1

    def __str__(self):
        return self.name


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    phone_number = db.Column(db.String(12))
    email_address = db.Column(db.String(100))
    password = db.Column(db.String(100))
    role = db.Column(sqlalchemy.types.Enum(Role))
    farmer_pid = db.Column(db.String(20))
    postings = db.relationship('Posting', backref='user', lazy=True)
    orders = db.relationship('Order', backref='user', lazy=True)
    profile_bio = db.Column(db.Text)

    def __init__(self, name, phoneNumber, emailAddress, password, role, profileBio):
        self.name = name
        self.phone_number = phoneNumber
        self.email_address = emailAddress
        self.password = password
        self.role = role
        self.farmer_pid = None
        self.creditCardNumber = None
        self.profile_bio = profileBio


class ShoppingCart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.relationship('User', backref='shopping_cart', lazy=True)
    items = db.relationship('Item', lazy=True)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
