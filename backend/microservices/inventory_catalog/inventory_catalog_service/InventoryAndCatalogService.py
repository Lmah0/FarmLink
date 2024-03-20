from flask import jsonify, request
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
            if 'userId' not in data or 'quantity' not in data or 'postingAuthor' not in data:
                return jsonify({'message': 'Invalid request: userId, quantity, and postingAuthor are required.'}), 400
        
            elif not isinstance(userId, int) or not isinstance(quantity, int):
                return jsonify({'message': 'Invalid values for userId or quantity.'}), 400
            elif quantity <= 0:
                return jsonify({'message': 'quantity must be greater than 0.'}), 400
            try:
                newPosting = models.Posting(userId, postingAuthor, quantity, imageFile, description) # Add to posting table
                
                models.db.session.add(newPosting)
                models.db.session.commit()
            except Exception as e:
                print(e)

            postingId = newPosting.id
            itemName = data['itemName']
            itemPrice = data['itemPrice']

            itemType = data['itemType']
        
            if 'itemName' not in data or 'itemPrice' not in data:
                return jsonify({'message': 'Invalid request: itemName, and itemPrice are required.'}), 400
            elif not isinstance(itemName, str) or not isinstance(itemPrice, (int, float)):
                return jsonify({'message': 'Invalid values for itemName or itemPrice.'}), 400
            elif itemPrice <= 0:
                return jsonify({'message': 'itemPrice must be greater than 0.'}), 400
            
            try:
                    itemType = models.ItemType[itemType]
            except KeyError:
                    return jsonify({'message': 'Invalid item type.'}), 400

            newItem = models.Item(itemName, itemPrice, itemType, postingId) # add to item table
                
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
        if 'postingId' not in data:
            return jsonify({'message': 'Invalid request: postingId is required.'}), 400
        elif not isinstance(postingId, int):
            return jsonify({'message': 'Invalid value for postingId.'}), 400
        elif postingId <= 0:
            return jsonify({'message': 'postingId must be greater than 0.'}), 400

        posting = models.Posting.query.filter_by(id=postingId).first()
        
        return jsonify(posting.serialize()), 200
    
    def getItem(self):
        itemId = request.args.get('itemId', "")  # Retrieve userID from query parameters
        if not itemId:
            return jsonify({'message': 'Invalid request: itemId is required.'}), 400
        try:
            itemId = int(itemId)
        except ValueError:
            return jsonify({'message': 'Invalid value for itemId.'}), 400
        
        if itemId <= 0:
            return jsonify({'message': 'itemId must be greater than 0.'}), 400
        
        item = models.Item.query.filter_by(id=itemId).first()
        
        return jsonify(item.serialize()), 200
    
    def removeStock(self):
        data = request.json
        postingId = data['postingId']
        quantity = data['quantity']

        if 'postingId' not in data or 'quantity' not in data:
            return jsonify({'message': 'Invalid request: postingId and quantity are required.'}), 400
        elif not isinstance(postingId, int) or not isinstance(quantity, int):
            return jsonify({'message': 'Invalid values for postingId or quantity.'}), 400
        elif postingId <= 0 or quantity <= 0:
            return jsonify({'message': 'postingId and quantity must be greater than 0.'}), 400
        
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