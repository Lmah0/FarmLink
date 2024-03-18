from flask import jsonify, request
from flask_cors import CORS
import json
from flask import Blueprint
from . import IInventoryAndCatalogService, models

main = Blueprint('main', __name__)

class InventoryAndCatalogService(IInventoryAndCatalogService.IInventoryAndCatalogService):
    def addPosting(self):
        try:
            # Check if the POST request has the file part
            imageFile = None
            try:
                imageFile = request.files['file'].read()
                print("Saving imageFile")
            except Exception as e:
                print("No image.")
            
            if 'userdata' not in request.form:
                return 'No user data', 400
            data = json.loads(request.form['userdata'])

            userId = data['userId']
            quantity = data['quantity']
            postingAuthor = data['postingAuthor']
            description = data['description']
            try:
                newPosting = models.Posting(userId, postingAuthor, quantity, imageFile, description)
                
                models.db.session.add(newPosting)
                models.db.session.commit()
            except Exception as e:
                print(e)

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

            # Optionally, you can return the file path or any other response
            return jsonify({'message': 'New posting added successfully'}), 200

        except Exception as e:
            return jsonify({'error': str(e)}), 500
        
        return jsonify({'message': 'File uploaded successfully'}), 200

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
        print("Item ID: ", itemId )
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

main.route('/addPosting', methods=['POST'])(inventoryAndCatalogService.addPosting)
main.route('/getPostings', methods=['GET'])(inventoryAndCatalogService.getPostings)
main.route('/getPosting', methods=['GET'])(inventoryAndCatalogService.getPosting)
main.get('/getItem')(inventoryAndCatalogService.getItem)
main.route('/removeStock', methods=['POST'])(inventoryAndCatalogService.removeStock)