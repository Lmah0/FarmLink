import os
from dotenv import load_dotenv

from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import requests
import json


load_dotenv()

ENVIRONMENT = 'production'

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

if ENVIRONMENT == 'development':
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/MegaMagaMagi'
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL').replace('postgres:', 'postgresql:')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


@app.route('/')
def hello_world():
    return 'Hello, World! This is the Database Service.'


if __name__ == '__main__':
    app.run(debug=True, port=5001)
