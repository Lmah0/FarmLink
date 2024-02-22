from . import db

class Order(db.Model):
    __tablename__ = 'maga_order'
    id = db.Column(db.Integer, primary_key=True)
    purchase_date = db.Column(db.DateTime, nullable=False)
    total_cost = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)

    def __init__(self, purchaseDate, totalCost, userId):
        self.purchase_date = purchaseDate
        self.total_cost = totalCost
        self.user_id = userId