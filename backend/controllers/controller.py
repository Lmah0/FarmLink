from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
import json

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# INSTRUCTIONS:
# 1. You need to use this file to control all the microservices to coordinate the payment as specified in the doc
# 2. You need to run each microservice at the same time, and call on the proper logic from within each microservice to complete the logic for this
     # When you run each microservice at the same time, you must specify different ports when you run each one (default is 5000 and we cannot run all microservices off the same port)

@app.route('/')
def hello_world():
    return 'Hello, World! This is the Controller for our application.'

@app.route('/checkStock', methods=['GET', "POST"])
def checkStock():
    data = request.json
    userID = data['userId']  
    itemID = data['itemId']   
    quantity = data['quantity'] 
    postingID = data['postingId']
    
    data = {"postingId": postingID}
    response = requests.get("http://127.0.0.1:5001/getPosting", json=data)   
    retrievedPosting = response.json() 
    print(f'The retrieved posting is {retrievedPosting}')

    if retrievedPosting['quantity'] < quantity:     # Check item is in stock (e.g., if quantity is available)
        return jsonify({'message': 'Not enough stock available.'}), 400
    else:
        # Process item (e.g., add it to the cart)
        data = {"userId": userID, "itemId": itemID, "quantity": quantity}
        requests.post("http://127.0.0.1:5002/addToCart", json=data)   
        return jsonify({'message': 'Sufficient stock'}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
