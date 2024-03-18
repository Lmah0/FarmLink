from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import requests
import json
from flask import Blueprint
from . import IInventoryAndCatalogService, models

main = Blueprint('main', __name__)

class InventoryAndCatalogService(IInventoryAndCatalogService.IInventoryAndCatalogService):
    def testing(self):
        return 'Hello, World! This is the Inventory and Catalog Service.'
    
    def addPosting(self):
        data = request.json

        userId = data['userId']
        quantity = data['quantity']
        postingAuthor = data['postingAuthor']
        description = data['description']

        if 'userId' not in data or 'quantity' not in data or 'postingAuthor' not in data:
            return jsonify({'message': 'Invalid request: userId, quantity, and postingAuthor are required.'}), 400
        
        elif not isinstance(userId, int) or not isinstance(quantity, int) or quantity <= 0:
            return jsonify({'message': 'Invalid values for userId or quantity.'}), 400

        newPosting = models.Posting(userId, postingAuthor, quantity, description) # Add to posting table
        
        models.db.session.add(newPosting)
        models.db.session.commit()

        postingId = newPosting.id
        itemName = data['itemName']
        itemPrice = data['itemPrice']

        itemType = data['itemType']

        if 'itemName' not in data or 'itemPrice' not in data:
            return jsonify({'message': 'Invalid request: itemName, and itemPrice are required.'}), 400
        elif not isinstance(itemName, str) or not isinstance(itemPrice, (int, float)) or itemPrice <= 0:
            return jsonify({'message': 'Invalid values for itemName or itemPrice.'}), 400
        
        try:
            itemType = models.ItemType[itemType]
        except KeyError:
            return jsonify({'message': 'Invalid item type.'}), 400

        newItem = models.Item(itemName, itemPrice, itemType, postingId) # add to item table
        
        models.db.session.add(newItem)
        models.db.session.commit()

        return jsonify({'message': 'New posting created!'}), 200

    def getPostings(self):
        postings = models.Posting.query.all()
        print(postings)
        
        return jsonify([posting.serialize() for posting in postings]), 200
    
    def getPosting(self):
        data = request.json
        postingId = data['postingId']

        posting = models.Posting.query.filter_by(id=postingId).first()
        
        return jsonify(posting.serialize()), 200
    
    def getItem(self):
        data = request.json
        itemId = data['itemId']

        item = models.Item.query.filter_by(id=itemId).first()
        
        return jsonify(item.serialize()), 200
    
    def removeStock(self):
        data = request.json
        postingId = data['postingId']
        quantity = data['quantity']

        # Remove Stock From Posting
        posting = models.Posting.query.filter_by(id=postingId).first()
        posting.quantity -= quantity
        models.db.session.commit()

        print("Stock removed!", posting.quantity)
        return jsonify({'message': 'Stock removed!'}), 200

    
inventoryAndCatalogService = InventoryAndCatalogService()

main.route('/', methods=['GET'])(inventoryAndCatalogService.testing)
main.route('/addPosting', methods=['POST'])(inventoryAndCatalogService.addPosting)
main.route('/getPostings', methods=['GET'])(inventoryAndCatalogService.getPostings)
main.route('/getPosting', methods=['GET'])(inventoryAndCatalogService.getPosting)
main.route('/getItem', methods=['POST'])(inventoryAndCatalogService.getItem)
main.route('/removeStock', methods=['POST'])(inventoryAndCatalogService.removeStock)

