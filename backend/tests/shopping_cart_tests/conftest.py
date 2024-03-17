import pytest

import pytest 
from microservices.shopping_cart_service import create_app, db

@pytest.fixture()
def setup():
    app = create_app()
    with app.app_context():
        db.create_all()
    
    yield app # stop here and run teardown after tests finish

    # Teardown

@pytest.fixture()
def client(app): # Simulate requests to service
    return app.test_client()