import pytest
from user_management.user_management_service import create_app, db

@pytest.fixture()
def app():
    app = create_app('test')
    with app.app_context():
        db.create_all()
    
    yield app # stop here and run teardown after tests finish

    # Teardown

@pytest.fixture()
def client(app): # Simulate requests to service
    return app.test_client()