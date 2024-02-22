from . import db


class ShoppingCart(db.Model):
    __tablename__ = 'shopping_cart'
    user_id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False, default=1)

    def __init__(self, user_id, item_id, quantity):
        self.user_id = user_id
        self.item_id = item_id
        self.quantity = quantity
