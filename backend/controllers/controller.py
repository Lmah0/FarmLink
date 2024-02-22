from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
import json

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# INSTRUCTIONS:
# 1. You need to use this file to control all the microservices to coordinate the payment as specified in the doc
# 2. You need to run each microservice at the same time, and call on the proper logic from within each microservice to complete the logic for this

@app.route('/')
def hello_world():
    return 'Hello, World! This is the Controller for our application.'

if __name__ == '__main__':
    app.run(debug=True, port=5001)