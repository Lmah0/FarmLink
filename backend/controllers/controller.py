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
    
    data = {"postingId": postingID}
    response = requests.get("http://127.0.0.1:5007/getPosting", json=data)   
    retrievedPosting = response.json() 
    print(f'The retrieved posting is {retrievedPosting}')

    if retrievedPosting['quantity'] < quantity:     # Check item is in stock (e.g., if quantity is available)
        return jsonify({'message': 'Not enough stock available.'}), 400
    else:
        # Process item (e.g., add it to the cart)
        data = {"userId": userID, "itemId": itemID, "quantity": quantity}
        requests.post("http://127.0.0.1:5008/addToCart", json=data)   
        return jsonify({'message': 'Sufficient stock'}), 200

@app.route('/createOrder', methods=['GET', "POST"])
def createOrder():
    data = request.json
    userID = data['userId']  
    
    # Get the cart
    data = {"userId": userID}
    response = requests.get(f"http://127.0.0.1:5008/returnCart", json=data)
    cart = response.json()

    print(cart)
 
    # Get the available stock of each item in the cart & sum the total cost
    totalCost = 0

    for item in cart:
       # Get the item from the database using the item ID
        itemId = item['itemId']
        print(itemId)
        data = {"itemId": itemId}
        response = requests.get(f"http://127.0.0.1:5007/getItem", json=data)
        retrievedItem = response.json()
        print(f'The retrieved item is {retrievedItem}')
        totalCost += retrievedItem['price'] * item['quantity']


        # Get the posting ID
        postingID = retrievedItem['posting_id']
        data = {"postingId": postingID}
        response = requests.get("http://127.0.0.1:5007/getPosting", json=data)
        retrievedPosting = response.json()
        print(f'The retrieved posting is {retrievedPosting}')
        # Check if the quantity in the cart is available

        if retrievedPosting['quantity'] < item['quantity']:
            return jsonify({'message': 'Not enough stock available.'}), 420 # 420 is a custom error code        
        else:
        #remove the quantity from the stock
            data = {"postingId": postingID, "quantity": item['quantity']}
            response = requests.post("http://127.0.0.1:5007/removeStock", json=data)
            print("The response is", response)

    # Create the order on the database using the cart
    data = {"userId": userID, "totalCost": totalCost}
    response = requests.post("http://127.0.0.1:5009/addOrder", json=data)

    # Flush the cart
                
    return jsonify({'message': 'Sufficient stock'}), 200


if __name__ == '__main__':
    app.run(debug=True, port=5000)
