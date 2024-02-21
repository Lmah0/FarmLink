from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import requests
import json
import os
from dotenv import load_dotenv
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

    db.init_app(app)

    @app.route('/')
    def hello_world():
        return 'Hello, World! This is the Inventory and Catalog Service.'

    from . import models

    @app.route('/db_create', methods=['GET'])
    def db_create():
        with app.app_context():
            db.create_all()

        return 'Tables Created!'

    @app.route('/db_example', methods=['POST', 'GET'])
    def db_example():
        if request.method == 'GET':
            return render_template('db_example.html')
        if request.method == 'POST':
            name = request.form['name']
            price = request.form['price']
            description = request.form['description']
            poster = request.form['poster']
            item_type = int(request.form['item_type'])

            posting = models.Posting(user_id=poster)
            db.session.add(posting)
            # Have to commit posting to assign it an id
            db.session.commit()
            item = models.Item(
                name=name, price=price, description=description, item_type=item_type, posting_id=posting.id)
            db.session.add(item)
            db.session.commit()
            return 'Posting created!'

    @app.route('/db_query/items_by_name/<item_name>', methods=['GET'])
    def db_query_item_by_name(item_name):
        items = models.Item.query.filter_by(name=item_name).all()
        if len(items) == 0:
            return 'Item not found!'
        return jsonify([item.serialize() for item in items])

    @app.route('/db_query/posting_by_id/<id>', methods=['GET'])
    def db_query_posting_by_id(id):
        posting = models.Posting.query.filter_by(id=id).first()
        if posting is None:
            return 'Posting not found!'
        return jsonify([posting.serialize()])

    return app
