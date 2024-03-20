import pytest

import pytest
from controllers.controller import app


# # Fixtures for inventory catalog
# @pytest.fixture()
# def app_inventory_catalog():
#     app_inventory_catalog = create_inventory_app('test')
#     with app_inventory_catalog.app_context():
#         inventory_db.create_all()
    
#     yield app_inventory_catalog # stop here and run teardown after tests finish

#     # Teardown

# @pytest.fixture()
# def client_inventory_catalog(app_inventory_catalog): # Simulate requests to service
#     return app_inventory_catalog.test_client()

# # Fixtures for shopping cart
# @pytest.fixture()
# def app_shopping_cart():
#     app_shopping_cart = create_shopping_cart_app('test')
#     with app_shopping_cart.app_context():
#         shopping_cart_db.create_all()
    
#     yield app_shopping_cart # stop here and run teardown after tests finish

#     # Teardown

# @pytest.fixture()
# def client_shopping_cart(app_shopping_cart): # Simulate requests to service
#     return app_shopping_cart.test_client()

# # Fixtures for checkout
# @pytest.fixture()
# def app_checkout():
#     app_checkout = create_checkout_app('test')
#     with app_checkout.app_context():
#         checkout_db.create_all()
    
#     yield app_checkout # stop here and run teardown after tests finish

#     # Teardown

# @pytest.fixture()
# def client_checkout(app_checkout): # Simulate requests to service
#     return app_checkout.test_client()

# # Fixture for controller
# @pytest.fixture
# def client_controller():
#     with app_controller.test_client() as client:
#         yield client

@pytest.fixture
def app_controller():
    return app 

@pytest.fixture
def client_controller(app_controller):
    with app_controller.test_client() as client:
        yield client


