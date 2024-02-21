from . import db

class ShoppingCart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.relationship('User', backref='shopping_cart', lazy=True)
    items = db.relationship('Item', lazy=True)


order_items = db.Table('order_items',
                       db.Column('order_id', db.Integer, db.ForeignKey('order.id')),
                       db.Column('item_id', db.Integer)
                       )