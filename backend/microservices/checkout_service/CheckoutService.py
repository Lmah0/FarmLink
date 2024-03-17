from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import requests
import json
from flask import Blueprint
from . import ICheckoutService, models
from datetime import datetime
import time
main = Blueprint('main', __name__)

class CheckoutService(ICheckoutService.ICheckoutService):
    def testing(self):
        return 'Hello, World! This is the Checkout Service.'
    
    def addOrder(self):
        data = request.json

        userId = data['userId']
        totalCost = data['totalCost']
        purchaseDate = datetime.now().replace(microsecond=0)

        newOrder = models.Order(purchaseDate, totalCost, userId)
        
        models.db.session.add(newOrder)
        models.db.session.commit()
        
        return jsonify({'message': 'New Order Created!'}), 200

checkoutService = CheckoutService()

main.route('/', methods=['GET'])(checkoutService.testing)
main.route('/addOrder', methods=['POST'])(checkoutService.addOrder)