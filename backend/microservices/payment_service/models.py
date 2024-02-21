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


class ShoppingCart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.relationship('User', backref='shopping_cart', lazy=True)
    items = db.relationship('Item', lazy=True)