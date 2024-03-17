from microservices.checkout_service.models import Order

def test_add_order_with_invalid_user_id(client, app): # use client to send simulated requests to service

    response = client.post('/addOrder', json={'userId': 1, 'totalCost': 100})
    assert response.status_code == 200

    with app.app_context():
        # Use this to verify something is being added to the DB
        assert Order.query.count() == 1

def test_add_order_with_valid_user_id_and_cost(client,app):
    pass

def test_add_order_with_invalid_cost(client,app):
    pass


        
