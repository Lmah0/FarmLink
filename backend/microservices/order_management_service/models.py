from . import db

class ShoppingCart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.relationship('User', backref='shopping_cart', lazy=True)
    items = db.relationship('Item', lazy=True)


order_items = db.Table('order_items',
                       db.Column('order_id', db.Integer, db.ForeignKey('order.id')),
                       db.Column('item_id', db.Integer)
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