from microservices.inventory_catalog_service.models import Item, Posting, ItemType
from microservices.inventory_catalog_service import db
import json
# Tests for addPosting
def test_add_posting_with_invalid_item_type(client, app): # use client to send simulated requests to service
    data = {
        'userdata': json.dumps({
            'userId': 1,
            'quantity': 100,
            'postingAuthor': 'Test',
            'description': 'Test',
            'itemName': 'Test',
            'itemPrice': 100,
            'itemType': 'INVALID'
        })
    }

    response = client.post('/addPosting', data=data)
    assert response.status_code == 400

    with app.app_context(): # Use this to verify something is being added to the DB
        assert Item.query.count() == 0

def test_add_posting_with_invalid_user_id(client, app):
    data = {
        'userdata': json.dumps({
            'userId': None,
            'quantity': 100,
            'postingAuthor': 'Test',
            'description': 'Test',
            'itemName': 'Test',
            'itemPrice': 100,
            'itemType': 'MACHINERY'
        })
    }
    response = client.post('/addPosting', data=data)
    assert response.status_code == 400

    with app.app_context():
        assert Item.query.count() == 0
        assert Posting.query.count() == 0

def test_add_posting_with_invalid_quantity(client, app):
    data = {
        'userdata': json.dumps({
            'userId': 1,
            'quantity': -100,
            'postingAuthor': 'Test',
            'description': 'Test',
            'itemName': 'Test',
            'itemPrice': 100,
            'itemType': 'MACHINERY'
        })
    }
    response = client.post('/addPosting', data=data)
    assert response.status_code == 400

    with app.app_context():
        assert Item.query.count() == 0
        assert Posting.query.count() == 0

def test_add_posting_with_invalid_item_price(client, app):
    data = {
        'userdata': json.dumps({
            'userId': 1,
            'quantity': 100,
            'postingAuthor': 'Test',
            'description': 'Test',
            'itemName': 'Test',
            'itemPrice': -100,
            'itemType': 'MACHINERY'
        })
    }
    response = client.post('/addPosting', data=data)
    assert response.status_code == 400

    with app.app_context():
        assert Item.query.count() == 0
        assert Posting.query.count() == 1

def test_add_posting_with_valid_input(client, app):
    data = {
        'userdata': json.dumps({
            'userId': 1,
            'quantity': 100,
            'postingAuthor': 'Test',
            'description': 'Test',
            'itemName': 'Test',
            'itemPrice': 100,
            'itemType': 'MACHINERY'
        })
    }
    response = client.post('/addPosting', data=data)
    assert response.status_code == 200

    with app.app_context():
        assert Item.query.count() == 1
        assert Posting.query.count() == 1

# Tests for getPostings
def test_get_postings(client, app):
# Add postings directly to the database
    with app.app_context():
        test_posting = Posting(
            user_id=1,
            posting_author='Test',
            quantity=100,
            description='Test',
            image=None
        )
        db.session.add(test_posting)

        test_item = Item(
        name = 'testItem',
        price = 100,
        item_type = 1,
        posting_id = 1
        )
        db.session.add(test_item)
        db.session.commit()

        
    response = client.get('/getPostings')
    assert response.status_code == 200

    with app.app_context():
        data = response.json
        assert data[0]['id'] == 1
        assert data[0]['quantity'] == 100
        assert data[0]['posting_author'] == 'Test'
        assert data[0]['description'] == 'Test'

# Tests for getPosting
def test_get_posting_with_invalid_posting_id(client, app):
    # Add postings directly to the database
    with app.app_context():
        test_posting = Posting(
            user_id=1,
            posting_author='Test',
            quantity=100,
            description='Test',
            image=None
        )
        db.session.add(test_posting)

        test_item = Item(
        name = 'testItem',
        price = 100,
        item_type = 1,
        posting_id = 1
        )
        db.session.add(test_item)
        db.session.commit()

        
    response = client.get('/getPosting', json={'postingId': None})
    assert response.status_code == 400

    with app.app_context():
        data = response.json
        assert data['message'] == 'Invalid value for postingId.'

def test_get_posting_with_valid_posting_id(client, app):
    # Add postings directly to the database
    with app.app_context():
        test_posting = Posting(
            user_id=1,
            posting_author='Test',
            quantity=100,
            description='Test',
            image=None
        )
        db.session.add(test_posting)

        test_item = Item(
        name = 'testItem',
        price = 100,
        item_type = 1,
        posting_id = 1
        )
        db.session.add(test_item)
        db.session.commit()

        
    response = client.get('/getPosting', json={'postingId': 1})
    assert response.status_code == 200

    with app.app_context():
        data = response.json
        assert data['id'] == 1
        assert data['quantity'] == 100
        assert data['posting_author'] == 'Test'
        assert data['description'] == 'Test'

# Tests for getItem
def test_get_item_with_invalid_item_id(client, app):
    # Add postings directly to the database
    with app.app_context():
        # Add a posting with userId=1
        test_posting = Posting(
            user_id=1,
            posting_author='Test',
            quantity=100,
            description='Test',
            image=None
        )
        db.session.add(test_posting)

        test_item = Item(
        name = 'testItem',
        price = 100,
        item_type = 1,
        posting_id = 1
        )
        db.session.add(test_item)
        db.session.commit()

        
    response = client.post('/getItem', json={'itemId': None})
    print(response)
    assert response.status_code == 400

    with app.app_context():
        data = response.json
        assert data['message'] == 'Invalid value for itemId.'

def test_get_item_with_valid_item_id(client, app):
    # Add postings directly to the database
    with app.app_context():
        # Add a posting with userId=1
        test_posting = Posting(
            user_id=1,
            posting_author='Test',
            quantity=100,
            description='Test',
            image=None
        )
        db.session.add(test_posting)

        test_item = Item(
        name = 'testItem',
        price = 100,
        item_type = 1,
        posting_id = 1
        )
        db.session.add(test_item)
        db.session.commit()

        
    response = client.post('/getItem', json={'itemId': 1})
    print(response)
    assert response.status_code == 200

    with app.app_context():
        data = response.json
        assert data['id'] == 1
        assert data['name'] == 'testItem'
        assert data['price'] == 100
        assert data['item_type'] == 'MACHINERY'
        assert data['posting_id'] == 1

# Tests for removeStock

def test_remove_stock_with_invalid_posting_id(client, app):
    # Add postings directly to the database
    with app.app_context():
        # Add a posting with userId=1
        test_posting = Posting(
            user_id=1,
            posting_author='Test',
            quantity=100,
            description='Test',
            image=None
        )
        db.session.add(test_posting)

        test_item = Item(
        name = 'testItem',
        price = 100,
        item_type = 1,
        posting_id = 1
        )
        db.session.add(test_item)
        db.session.commit()

        
    response = client.post('/removeStock', json={'postingId': None, 'quantity': 100})
    assert response.status_code == 400

    with app.app_context():
        data = response.json
        assert data['message'] == 'Invalid values for postingId or quantity.'
        posting = Posting.query.filter_by(id=1).first()
        assert posting.quantity == 100

def test_remove_stock_with_invalid_quantity(client, app):
    with app.app_context():
        test_posting = Posting(
            user_id=1,
            posting_author='Test',
            quantity=100,
            description='Test',
            image=None
        )
        db.session.add(test_posting)

        test_item = Item(
        name = 'testItem',
        price = 100,
        item_type = 1,
        posting_id = 1
        )
        db.session.add(test_item)
        db.session.commit()

        
    response = client.post('/removeStock', json={'postingId': 1, 'quantity': -100})
    assert response.status_code == 400

    with app.app_context():
        data = response.json
        assert data['message'] == 'postingId and quantity must be greater than 0.'
        posting = Posting.query.filter_by(id=1).first()
        assert posting.quantity == 100

def test_remove_stock_with_valid_input(client, app):
    with app.app_context():
        test_posting = Posting(
            user_id=1,
            posting_author='Test',
            quantity=100,
            description='Test',
            image=None
        )
        db.session.add(test_posting)

        test_item = Item(
        name = 'testItem',
        price = 100,
        item_type = 1,
        posting_id = 1
        )
        db.session.add(test_item)
        db.session.commit()

        
    response = client.post('/removeStock', json={'postingId': 1, 'quantity': 100})
    assert response.status_code == 200

    with app.app_context():
        data = response.json
        assert data['message'] == 'Stock removed!'
        posting = Posting.query.filter_by(id=1).first()
        assert posting.quantity == 0