from flask import jsonify, request
from flask_cors import CORS
from flask import Blueprint
from . import ICheckoutService, models

import time
main = Blueprint('main', __name__)

class CheckoutService(ICheckoutService.ICheckoutService):
    def addOrder(self):
        data = request.json

        userId = data['userId']
        totalCost = data['totalCost']
        purchaseDate = time.strftime('%Y-%m-%d %H:%M:%S')

        newOrder = models.Order(purchaseDate, totalCost, userId)
        
        models.db.session.add(newOrder)
        models.db.session.commit()
        
        return jsonify({'message': 'New Order Created!'}), 200

checkoutService = CheckoutService()

main.route('/addOrder', methods=['POST'])(checkoutService.addOrder)