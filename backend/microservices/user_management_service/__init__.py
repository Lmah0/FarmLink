from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
import json
import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

ENVIRONMENT = 'development'
db = SQLAlchemy()

# To run: 'flask --app user_management_service run --debug' in console
def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "*"}})
    app.config.from_pyfile('config.py', silent=True)
    if ENVIRONMENT == 'production':
        load_dotenv()
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL').replace('postgres:', 'postgresql:')

    db.init_app(app)

    from . import models

    # TODO: Remove method before deploying
    @app.route('/db_reset', methods=['GET'])
    def db_create():
        db.session.execute(text("DROP TABLE IF EXISTS maga_user;"))
        db.session.commit()
        with app.app_context():
            db.create_all()

        return 'Tables Reset!'

    @app.route('/')
    def hello_world():
        return 'Hello, World! This is the User Management Service.'

    return app
