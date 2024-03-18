from flask import jsonify, request
from flask_cors import CORS
from flask import Blueprint
from . import ICheckoutService, models
from datetime import datetime
import time
main = Blueprint('main', __name__)

class CheckoutService(ICheckoutService.ICheckoutService):
    def addOrder(self):
        data = request.json
        # Check if userId and totalCost are present and have valid values
        if 'userId' not in data or 'totalCost' not in data:
            return jsonify({'message': 'Invalid request: userId and totalCost are required.'}), 400

        userId = data['userId']
        totalCost = data['totalCost']

        # Validate userId and totalCost 
        if not isinstance(userId, int) or not isinstance(totalCost, (int, float)):
            return jsonify({'message': 'Invalid values for userId or totalCost.'}), 400
        elif totalCost <= 0:
            return jsonify({'message': 'totalCost must be greater than 0.'}), 400

        # Create purchaseDate
        purchaseDate = datetime.now().replace(microsecond=0)

        try:
            newOrder = models.Order(purchaseDate, totalCost, userId)
            models.db.session.add(newOrder)
            models.db.session.commit()
            return jsonify({'message': 'New Order Created!'}), 200
        except Exception as e:
            # Handle any unexpected errors
            return jsonify({'message': f'Error creating order: {str(e)}'}), 500

checkoutService = CheckoutService()

main.route('/addOrder', methods=['POST'])(checkoutService.addOrder)