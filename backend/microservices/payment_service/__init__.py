import os

from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
import json

from flask_sqlalchemy import SQLAlchemy

ENVIRONMENT = 'development'
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "*"}})
    app.config.from_pyfile('config.py', silent=True)
    if ENVIRONMENT == 'production':
        load_dotenv()
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL').replace('postgres:', 'postgresql:')

    from . import models

    @app.route('/db_create', methods=['GET'])
    def db_create():
        with app.app_context():
            db.create_all()

        return 'Tables Created!'

    @app.route('/')
    def hello_world():
        return 'Hello, World! This is the Payment Service.'

    return app