from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import requests
import json
from flask import Blueprint
from . import IInventoryAndCatalogService, models
import os

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
    
    def uploadImage(self):
        try:
            # Check if the POST request has the file part
            if 'file' not in request.files:
                return 'No file part', 400

            imageFile = request.files['file']

            if not imageFile:
                print("What is file")
                return jsonify({'error': 'No file part'}), 400

            # If the user does not select a file, the browser submits an empty file without a filename
            if imageFile.filename == '':
                return jsonify({'error': 'No selected file'}), 400

            # Specify the directory where you want to save the uploaded images
            upload_directory = './'

            # If the directory doesn't exist, create it
            if not os.path.exists(upload_directory):
                os.makedirs(upload_directory)

            # Save the file to the specified directory
            imageFile.save(os.path.join(upload_directory, imageFile.filename))

            # Optionally, you can return the file path or any other response
            return jsonify({'message': 'File uploaded successfully', 'file_path': os.path.join(upload_directory, imageFile.filename)}), 200

        except Exception as e:
            print("ERROR HTEE")
            print(e)
            return jsonify({'error': str(e)}), 500
        
        return jsonify({'message': 'File uploaded successfully'}), 200

    def getImage(self):
        pass

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
main.route('/uploadImage', methods=['POST'])(inventoryAndCatalogService.uploadImage)
