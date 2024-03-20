from flask import Flask, jsonify
from flask_cors import CORS
import os, json
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from flask_swagger_ui import get_swaggerui_blueprint

ENVIRONMENT = 'development'
db = SQLAlchemy()

# To run: 'flask --app user_management_service run --debug' in console
# To run on a specific port: 'flask --app user_management_service run --debug --port 5000' in console

def create_app(ENVIRONMENT='development'):
    app = Flask(__name__)
    # CORS(app, resources={r"/*": {"origins": "*"}})
    CORS(app)

    # Configure Swagger UI
    SWAGGER_URL = '/swagger'
    API_URL = 'http://127.0.0.1:5000/swagger.json'
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
        with open('./user_management_service/swagger.json', 'r') as f:
            return jsonify(json.load(f))

    app.config.from_pyfile('config.py', silent=True)
    if ENVIRONMENT == 'production':
        load_dotenv()
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL').replace('postgres:', 'postgresql:')
    elif ENVIRONMENT == 'test': # Create DB in memory so that production DB is not affected during tests
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    db.init_app(app)

    from . import models
    from . import UserManagementService

    app.register_blueprint(UserManagementService.main)

    # TODO: Remove method before deploying
    @app.route('/db_reset', methods=['GET'])
    def db_create():
        db.session.execute(text("DROP TABLE IF EXISTS maga_user;"))
        db.session.commit()
        with app.app_context():
            db.create_all()

        return 'Tables Reset!'

    return app
