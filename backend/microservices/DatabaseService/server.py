from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import requests
import json


ENVIRONMENT = 'development'

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

if ENVIRONMENT == 'development':
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/MegaMagaMagi'
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class TestModel(db.Model):
    __tablename__ = 'test_model'
    id = db.Column(db.Integer, primary_key=True)
    entry = db.Column(db.String(100), unique=True)

    def __init__(self, entry):
        self.entry = entry


@app.route('/')
def hello_world():
    return 'Hello, World! This is the Database Service.'


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=5001)
