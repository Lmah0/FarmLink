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

        newPosting = models.Posting(userId, postingAuthor, quantity, description)
        
        models.db.session.add(newPosting)
        models.db.session.commit()

        postingId = newPosting.id
        itemName = data['itemName']
        itemPrice = data['itemPrice']

        itemType = data['itemType']
        try:
            itemType = models.ItemType[itemType]
        except KeyError:
            return jsonify({'message': 'Invalid item type.'})

        newItem = models.Item(itemName, itemPrice, itemType, postingId)
        
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
    
inventoryAndCatalogService = InventoryAndCatalogService()

main.route('/', methods=['GET'])(inventoryAndCatalogService.testing)
main.route('/addPosting', methods=['POST'])(inventoryAndCatalogService.addPosting)
main.route('/getPostings', methods=['GET'])(inventoryAndCatalogService.getPostings)
main.route('/getPosting', methods=['GET'])(inventoryAndCatalogService.getPosting)