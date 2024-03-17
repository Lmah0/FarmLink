from microservices.checkout_service.models import Order

def test_add_order_with_invalid_user_id(client, app): # use client to send simulated requests to service

    response = client.get('/')
    assert response.data == b'Hello, World! This is the Checkout Service.'

    response = client.post('/addOrder', json={'userId': 1, 'totalCost': 100})
    assert response.status_code == 200
    assert response.json == {'message': 'New Order Created!'}

    response = client.post('/addOrder', json={'userId': 2, 'totalCost': 200})
    assert response.status_code == 200
    assert response.json == {'message': 'New Order Created!'}

    with app.app_context():
        # Use this to verify something is being added to the DB
        assert Order.query.count() == 2


    
        
