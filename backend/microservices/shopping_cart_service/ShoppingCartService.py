from flask import jsonify, request
from flask_cors import CORS
from flask import Blueprint
from . import IShoppingCartService, models

main = Blueprint('main', __name__)

class ShoppingCartService(IShoppingCartService.IShoppingCartService):
    def addToCart(self):
        data = request.json
        userID = data['userId']  
        itemID = data['itemId']   
        quantity = data['quantity'] 
                    
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
            
        # Retrieve the shopping cart item to delete
        shoppingCartItem = models.ShoppingCart.query.filter_by(user_id=userID, item_id=itemID, quantity=quantity).first()
        
        if shoppingCartItem is None: # Check if item is in cart
            return jsonify({'message': 'Item not found in cart.'}), 404
        else:
            # Process item (e.g., remove it from the cart)
            models.db.session.delete(shoppingCartItem)
            models.db.session.commit()

            return jsonify({'message': 'Items removed from cart successfully.'})

    def returnCart(self):
        data = request.json
        userID = data['userId']  
        items = models.ShoppingCart.query.filter_by(user_id=userID).all() # Access the list of items under the User ID
        print(f"The Items are {items}")

        return jsonify([item.serialize() for item in items]), 200        

    def flushCart(self):
        data = request.json
        userID = data['userId']

        shoppingCartItems = models.ShoppingCart.query.filter_by(user_id=userID).all() # Retrieve all items for the specified user ID
        
        if not shoppingCartItems:  # Check if there are no items for the specified user ID
            return jsonify({'message': 'No items found in cart for the specified user ID.'}), 404
    
        # Process each item (e.g., remove it from the cart)
        for item in shoppingCartItems:
            models.db.session.delete(item)
    
        # Commit the changes to the database
        models.db.session.commit()

        return jsonify({'message': 'All items removed from cart successfully.'}), 200

shoppingCartService = ShoppingCartService()

main.route('/addToCart', methods=['POST'])(shoppingCartService.addToCart)
main.route('/removeFromCart', methods=['DELETE'])(shoppingCartService.removeFromCart)
main.route('/returnCart', methods=['POST'])(shoppingCartService.returnCart)
main.route('/flushCart', methods=['DELETE'])(shoppingCartService.flushCart)