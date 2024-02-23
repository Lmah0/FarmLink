from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import requests
import json
from flask import Blueprint
from . import IShoppingCartService, models

main = Blueprint('main', __name__)

class ShoppingCartService(IShoppingCartService.IShoppingCartService):
    def testing(self):
        return 'Hello, World! This is the Shopping Cart Service.'
    
    def addToCart(self):
        data = request.json
        userID = data['userId']  
        itemID = data['itemId']   
        quantity = data['quantity'] 

        # Check item is in stock (e.g., if quantity is available)
            
        # Process item (e.g., add it to the cart)
        newShoppingCartItem = models.ShoppingCart(userID, itemID, quantity)
        models.db.session.add(newShoppingCartItem)
        models.db.session.commit()

        return jsonify({'message': 'Items added to cart successfully.'})


    def removeFromCart(self):
        data = request.json
        userID = data['userId']  
        itemID = data['itemId']  
        quantity = data['quantity']
        
        # Process each item (e.g., remove it from the cart)
        newShoppingCartItem = models.ShoppingCart(userID, itemID, quantity)
        models.db.session.delete(newShoppingCartItem)
        models.db.session.commit()

        return jsonify({'message': 'Items removed from cart successfully.'})

    def returnCart(self):
        data = request.json
        userID = data['userId']  
        items = models.Posting.query.filter_by(user_id=userID).all() # Access the list of items under the User ID
        print(items)

        return jsonify([items.serialize() for item in items]), 200        

    def flushCart(self):
        data = request.json
        userID = data['userId']
        models.ShoppingCart.query.filter_by(user_id=userID).delete() # delete all items in cart for a user
        return jsonify({'message': 'Cart flushed successfully.'})

shoppingCartService = ShoppingCartService()

main.route('/', methods=['GET'])(shoppingCartService.testing)
main.route('/addToCart', methods=['POST'])(shoppingCartService.addToCart)
main.route('/removeFromCart', methods=['DELETE'])(shoppingCartService.removeFromCart)
main.route('/returnCart', methods=['GET'])(shoppingCartService.returnCart)
main.route('/flushCart', methods=['DELETE'])(shoppingCartService.flushCart)