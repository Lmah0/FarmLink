import pytest

import pytest 
from microservices.checkout_service import create_app, db

@pytest.fixture()
def app():
    app = create_app()
    with app.app_context():
        db.create_all()
    
    yield app # stop here and run teardown after tests finish

    # Teardown

@pytest.fixture()
def client(setup): # Simulate requests to service
    return setup.test_client()