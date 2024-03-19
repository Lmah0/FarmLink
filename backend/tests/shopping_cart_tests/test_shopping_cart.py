from microservices.shopping_cart_service.models import ShoppingCart
from microservices.shopping_cart_service import db
import json
# Tests for addToCart
def test_add_to_cart_with_invalid_user_id(client, app): # use client to send simulated requests to service
    data = {
        "userId": "1",
        "itemId": 1,
        "quantity": 1
    }
    response = client.post('/addToCart', json=data)
    assert response.status_code == 400
    assert b'Invalid values for userId, itemId, or quantity.' in response.data
    with app.app_context():
        assert ShoppingCart.query.count() == 0

def test_add_to_cart_with_invalid_item_id(client, app):
    data = {
        "userId": 1,
        "itemId": "1",
        "quantity": 1
    }
    response = client.post('/addToCart', json=data)
    assert response.status_code == 400
    assert b'Invalid values for userId, itemId, or quantity.' in response.data
    with app.app_context():
        assert ShoppingCart.query.count() == 0    

def test_add_to_cart_with_invalid_quantity(client, app):
    data = {
        "userId": 1,
        "itemId": 1,
        "quantity": -1
    }
    response = client.post('/addToCart', json=data)
    assert response.status_code == 400
    assert b'Quantity must be greater than 0.' in response.data
    with app.app_context():
        assert ShoppingCart.query.count() == 0
def test_add_to_cart_with_valid_values(client, app):
    data = {
        "userId": 1,
        "itemId": 1,
        "quantity": 1
    }
    response = client.post('/addToCart', json=data)
    assert response.status_code == 200
    assert b'Items added to cart successfully.' in response.data
    with app.app_context():
        assert ShoppingCart.query.count() == 1
        cart_item = ShoppingCart.query.first()
        assert cart_item.user_id == 1
        assert cart_item.item_id == 1
        assert cart_item.quantity == 1


# Tests for removeFromCart
def test_remove_from_cart_with_invalid_user_id(client, app):
    test_cart = ShoppingCart(1, 1, 1)
    with app.app_context():
        db.session.add(test_cart)
        db.session.commit()

    data = {
        "userId": None,
        "itemId": 1,
    }
    response = client.delete('/removeFromCart', json=data)
    assert response.status_code == 400
    assert b'Invalid values for userId, or itemId' in response.data
    with app.app_context():
        assert ShoppingCart.query.count() == 1

def test_remove_from_cart_with_invalid_item_id(client, app):
    test_cart = ShoppingCart(1, 1, 1)
    with app.app_context():
        db.session.add(test_cart)
        db.session.commit()

    data = {
        "userId": 1,
        "itemId": None,
    }
    response = client.delete('/removeFromCart', json=data)
    assert response.status_code == 400
    assert b'Invalid values for userId, or itemId' in response.data
    with app.app_context():
        assert ShoppingCart.query.count() == 1


def test_remove_from_cart_with_item_not_in_cart(client, app):
    test_cart = ShoppingCart(1, 1, 1)
    with app.app_context():
        db.session.add(test_cart)
        db.session.commit()

    data = {
        "userId": 2,
        "itemId": 2,
        "quantity": 2
    }
    response = client.delete('/removeFromCart', json=data)
    assert response.status_code == 400
    assert b'Item not found in cart.' in response.data
    with app.app_context():
        assert ShoppingCart.query.count() == 1

def test_remove_from_cart_with_valid_values(client, app):
    test_cart = ShoppingCart(1, 1, 1)
    with app.app_context():
        db.session.add(test_cart)
        db.session.commit()

    data = {
        "userId": 1,
        "itemId": 1,
        "quantity": 1
    }
    response = client.delete('/removeFromCart', json=data)
    assert response.status_code == 200
    assert b'Items removed from cart successfully.' in response.data
    with app.app_context():
        assert ShoppingCart.query.count() == 0

# Tests for returnCart
def test_return_cart_with_invalid_user_id(client, app):

    response = client.get(f'/returnCart?userId={None}')
    assert response.status_code == 400
    assert b'Invalid value for userId.' in response.data

def test_return_cart_with_valid_values(client, app):
    test_cart = ShoppingCart(1, 1, 1)
    with app.app_context():
        db.session.add(test_cart)
        db.session.commit()


    response = client.get(f'/returnCart?userId={1}')
    assert response.status_code == 200
    data = response.json 
    assert data[0]['userId'] == 1
    assert data[0]['itemId'] == 1
    assert data[0]['quantity'] == 1

# Tests for flushCart
def test_flush_cart_with_invalid_user_id(client, app):
    test_cart = ShoppingCart(1, 1, 1)
    with app.app_context():
        db.session.add(test_cart)
        db.session.commit()

    response = client.delete('/flushCart', json={"userId": None})
    assert response.status_code == 400
    assert b'Invalid value for userId.' in response.data
    with app.app_context():
        assert ShoppingCart.query.count() == 1

def test_flush_cart_with_valid_values(client, app):
    test_cart = ShoppingCart(1, 1, 1)
    with app.app_context():
        db.session.add(test_cart)
        db.session.commit()

    response = client.delete('/flushCart', json={"userId": 1})
    assert response.status_code == 200
    assert b'All items removed from cart successfully.' in response.data
    with app.app_context():
        assert ShoppingCart.query.count() == 0

def test_flush_cart_with_no_items(client, app):
    response = client.delete('/flushCart', json={"userId": 1})
    assert response.status_code == 404
    assert b'No items found in cart for the specified user ID.' in response.data
    with app.app_context():
        assert ShoppingCart.query.count() == 0