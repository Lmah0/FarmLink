import os

from flask import Flask, jsonify, request
from flask_cors import CORS
import requests, json
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Run in directory controllers/ with command: flask --app controller run --debug --port 5002

SWAGGER_URL = '/swagger'
API_URL = 'http://127.0.0.1:5002/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "API Documentation"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

USR_URL = os.environ.get('USR_URL', 'http://127.0.0.1:5006')
INV_URL = os.environ.get('INV_URL', 'http://127.0.0.1:5007')
SHP_URL = os.environ.get('SHP_URL', 'http://127.0.0.1:5008')
CHK_URL = os.environ.get('CHK_URL', 'http://127.0.0.1:5009')


@app.route('/swagger.json')
def swagger():
    with open('../controllers/swagger.json', 'r') as f:
        return jsonify(json.load(f))
        
@app.route('/checkStock', methods=['GET', "POST"])
def checkStock():
    data = request.json
    userID = data['userId']  
    itemID = data['itemId']   
    quantity = data['quantity'] 
    postingID = data['postingId']

    if not userID or not itemID or not quantity or not postingID:
        return jsonify({'message': 'Invalid request: userId, itemId, quantity, and postingId are required.'}), 400
    elif not isinstance(userID, int) or not isinstance(itemID, int) or not isinstance(quantity, int) or not isinstance(postingID, int):
        return jsonify({'message': 'Invalid values for userId, itemId, quantity, or postingId.'}), 400
    elif quantity <= 0:
        return jsonify({'message': 'Quantity must be greater than 0.'}), 400
    
    data = {"postingId": postingID}
    response = requests.get(INV_URL + "/getPosting", json=data)
    if response.status_code != 200:
        return jsonify({'message': 'Error in retrieving posting.'}), 400
    
    retrievedPosting = response.json() 
    print(f'The retrieved posting is {retrievedPosting}')

    if retrievedPosting['quantity'] < quantity:     # Check item is in stock (e.g., if quantity is available)
        return jsonify({'message': 'Not enough stock available.'}), 400
    else:
        # Process item (e.g., add it to the cart)
        data = {"userId": userID, "itemId": itemID, "quantity": quantity}
        requests.post(SHP_URL + "/addToCart", json=data)
        return jsonify({'message': 'Sufficient stock'}), 200

@app.route('/createOrder', methods=['GET', "POST"])
def createOrder():
    data = request.json
    userID = data['userId']  
    
    if not userID:
        return jsonify({'message': 'Invalid request: userId is required.'}), 400
    elif not isinstance(userID, int):
        return jsonify({'message': 'Invalid value for userId.'}), 400

    # Get the cart
    data = {"userId": userID}
    response = requests.get(f"{SHP_URL}/returnCart?userId={userID}")
    if response.status_code != 200:
        return jsonify({'message': 'Error in retrieving cart.'}), 400
    cart = response.json()

    print(cart)
 
    # Get the available stock of each item in the cart & sum the total cost
    totalCost = 0

    for item in cart:
       # Get the item from the database using the item ID
        itemId = item['itemId']
        print(f"The ItemID is: {itemId}")
        data = {"itemId": itemId}
        response = requests.get(f"{INV_URL}/getItem?itemId={itemId}")
        retrievedItem = response.json()
        print(f'The retrieved item is {retrievedItem}')
        totalCost += retrievedItem['price'] * item['quantity']


        # Get the posting ID
        postingID = retrievedItem['posting_id']
        data = {"postingId": postingID}
        response = requests.get(INV_URL + "/getPosting", json=data)
        retrievedPosting = response.json()
        print(f'The retrieved posting is {retrievedPosting}')
        # Check if the quantity in the cart is available

        if retrievedPosting['quantity'] < item['quantity']:
            return jsonify({'message': 'Not enough stock available.'}), 420 # 420 is a custom error code        
        else:
        #remove the quantity from the stock
            data = {"postingId": postingID, "quantity": item['quantity']}
            response = requests.post(INV_URL + "/removeStock", json=data)
            print("The response is", response)
        # Flushing Cart
            data = {"userId": userID}
            response = requests.delete(SHP_URL + "/flushCart", json=data)
            print("The response is", response)    

    # Create the order on the database using the cart
    data = {"userId": userID, "totalCost": totalCost}
    response = requests.post(CHK_URL + "/addOrder", json=data)


                
    return jsonify({'message': 'Sufficient stock'}), 200


if __name__ == '__main__':
    app.run(debug=True, port=5000)
