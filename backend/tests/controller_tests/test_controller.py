import responses 

# Tests for checkStock
@responses.activate
def test_check_stock_with_invalid_user_id(client_controller): # use client to send simulated requests to service
    posting_item = {
        "id": 1,
        "item_type": "PRODUCE",
        "name": "test_item",
        "posting_id": 1
    }
    responses.add( # Use to mock response from API
        responses.GET,
        "http://127.0.0.1:5007/getPosting", 
        json={"description": "test", "id": 1, "image": None, "posting_author": "test_author", "posting_item": posting_item , "quantity": 3, "user_id": 1 }, # response 
        status=200
    ) 

    responses.add(
        responses.POST,
        "http://127.0.0.1:5008/addToCart", 
        status=200
    )
    response = client_controller.post('/checkStock', json={'userId': None, 'itemId': 1, 'quantity': 3, "postingId": 1}) 
    assert response.status_code == 400
    data = response.json
    assert data['message'] == 'Invalid request: userId, itemId, quantity, and postingId are required.'
    
@responses.activate
def test_check_stock_with_invalid_item_id(client_controller): # use client to send simulated requests to service
    posting_item = {
        "id": 1,
        "item_type": "PRODUCE",
        "name": "test_item",
        "posting_id": 1
    }
    responses.add( # Use to mock response from API
        responses.GET,
        "http://127.0.0.1:5007/getPosting", 
        json={"description": "test", "id": 1, "image": None, "posting_author": "test_author", "posting_item": posting_item , "quantity": 3, "user_id": 1 }, # response 
        status=200
    ) 

    responses.add(
        responses.POST,
        "http://127.0.0.1:5008/addToCart", 
        status=200
    )
    response = client_controller.post('/checkStock', json={'userId': 1, 'itemId': None, 'quantity': 3, "postingId": 1}) 
    assert response.status_code == 400
    data = response.json
    assert data['message'] == 'Invalid request: userId, itemId, quantity, and postingId are required.'
    
@responses.activate
def test_check_stock_with_invalid_quantity(client_controller): # use client to send simulated requests to service
    posting_item = {
        "id": 1,
        "item_type": "PRODUCE",
        "name": "test_item",
        "posting_id": 1
    }
    responses.add( # Use to mock response from API
        responses.GET,
        "http://127.0.0.1:5007/getPosting", 
        json={"description": "test", "id": 1, "image": None, "posting_author": "test_author", "posting_item": posting_item , "quantity": 3, "user_id": 1 }, # response 
        status=200
    ) 

    responses.add(
        responses.POST,
        "http://127.0.0.1:5008/addToCart", 
        status=200
    )
    response = client_controller.post('/checkStock', json={'userId': 1, 'itemId': 1, 'quantity': -3, "postingId": 1}) 
    assert response.status_code == 400
    data = response.json
    assert data['message'] == 'Quantity must be greater than 0.'

@responses.activate
def test_check_stock_with_insufficient_stock(client_controller): # use client to send simulated requests to service
    posting_item = {
        "id": 1,
        "item_type": "PRODUCE",
        "name": "test_item",
        "posting_id": 1
    }
    responses.add( # Use to mock response from API
        responses.GET,
        "http://127.0.0.1:5007/getPosting", 
        json={"description": "test", "id": 1, "image": None, "posting_author": "test_author", "posting_item": posting_item , "quantity": 1, "user_id": 1 }, # response 
        status=200
    ) 

    responses.add(
        responses.POST,
        "http://127.0.0.1:5008/addToCart", 
        status=200
    )
    response = client_controller.post('/checkStock', json={'userId': 1, 'itemId': 1, 'quantity': 3, "postingId": 1}) 
    assert response.status_code == 400
    data = response.json
    assert data['message'] == 'Not enough stock available.'

@responses.activate
def test_check_stock_with_sufficient_stock(client_controller): # use client to send simulated requests to service

    posting_item = {
        "id": 1,
        "item_type": "PRODUCE",
        "name": "test_item",
        "posting_id": 1
    }
    responses.add( # Use to mock response from API
        responses.GET,
        "http://127.0.0.1:5007/getPosting", 
        json={"description": "test", "id": 1, "image": None, "posting_author": "test_author", "posting_item": posting_item , "quantity": 3, "user_id": 1 }, # response 
        status=200
    ) 

    responses.add(
        responses.POST,
        "http://127.0.0.1:5008/addToCart", 
        status=200
    )
    response = client_controller.post('/checkStock', json={'userId': 1, 'itemId': 1, 'quantity': 3, "postingId": 1}) 
    assert response.status_code == 200
    data = response.json
    assert data['message'] == 'Sufficient stock'

# Tests for createOrder
@responses.activate
def test_create_order_with_invalid_posting_id(client_controller): # use client to send simulated requests to service
    cart_data = [
        {
            "itemId": 2,
            "quantity": 2,
            "userId": 2
        }
    ]
    responses.add( # Use to mock response from API
        responses.GET,
        f"http://127.0.0.1:5008/returnCart?userId={1}", 
        json = cart_data,
        status=200
    ) 

    responses.add( # Use to mock response from API
        responses.GET,
        f"http://127.0.0.1:5007/getItem?itemId={1}", 
        json = {
            "id": 1,
            "item_type": "PRODUCE",
            "name": "test",
            "posting_id": 1,
            "price": 1
        },
        status=200
    ) 
    
    posting_item = {
        "id": 1,
        "item_type": "PRODUCE",
        "name": "test_item",
        "posting_id": 1
    }
    responses.add( # Use to mock response from API
        responses.GET,
        "http://127.0.0.1:5007/getPosting", 
        json={"description": "test", "id": 1, "image": None, "posting_author": "test_author", "posting_item": posting_item , "quantity": 1, "user_id": 1 }, # response 
        status=200
    ) 
    
    
    responses.add( # Use to mock response from API
        responses.POST,
        "http://127.0.0.1:5007/removeStock", 
        status=200
    ) 
    
    responses.add( # Use to mock response from API
        responses.DELETE,
        "http://127.0.0.1:5008/flushCart", 
        status=200
    ) 

    responses.add( # Use to mock response from API
        responses.POST,
        "http://127.0.0.1:5009/addOrder", 
        status=200
    ) 
    
    response = client_controller.post('/createOrder', json={'userId': None}) 
    assert response.status_code == 400
    data = response.json
    assert data['message'] == 'Invalid request: userId is required.'

@responses.activate
def test_create_order_with_insufficient_stock(client_controller): # use client to send simulated requests to service
    cart_data = [
        {
            "itemId": 1,
            "quantity": 2,
            "userId": 1
        }
    ]
    responses.add( # Use to mock response from API
        responses.GET,
        f"http://127.0.0.1:5008/returnCart?userId={1}", 
        json = cart_data,
        status=200
    ) 

    responses.add( # Use to mock response from API
        responses.GET,
        f"http://127.0.0.1:5007/getItem?itemId={1}", 
        json = {
            "id": 1,
            "item_type": "PRODUCE",
            "name": "test",
            "posting_id": 1,
            "price": 1
        },
        status=200
    ) 
    
    posting_item = {
        "id": 1,
        "item_type": "PRODUCE",
        "name": "test_item",
        "posting_id": 1
    }
    responses.add( # Use to mock response from API
        responses.GET,
        "http://127.0.0.1:5007/getPosting", 
        json={"description": "test", "id": 1, "image": None, "posting_author": "test_author", "posting_item": posting_item , "quantity": 0, "user_id": 1 }, # response 
        status=200
    ) 
    
    
    responses.add( # Use to mock response from API
        responses.POST,
        "http://127.0.0.1:5007/removeStock", 
        status=200
    ) 
    
    responses.add( # Use to mock response from API
        responses.DELETE,
        "http://127.0.0.1:5008/flushCart", 
        status=200
    ) 

    responses.add( # Use to mock response from API
        responses.POST,
        "http://127.0.0.1:5009/addOrder", 
        status=200
    ) 
    
    response = client_controller.post('/createOrder', json={'userId': 1}) 
    assert response.status_code == 420
    data = response.json
    assert data['message'] == 'Not enough stock available.'

@responses.activate
def test_create_order_with_sufficient_stock(client_controller): # use client to send simulated requests to service
    cart_data = [
        {
            "itemId": 1,
            "quantity": 2,
            "userId": 1
        }
    ]
    responses.add( # Use to mock response from API
        responses.GET,
        f"http://127.0.0.1:5008/returnCart?userId={1}", 
        json = cart_data,
        status=200
    ) 

    responses.add( # Use to mock response from API
        responses.GET,
        f"http://127.0.0.1:5007/getItem?itemId={1}", 
        json = {
            "id": 1,
            "item_type": "PRODUCE",
            "name": "test",
            "posting_id": 1,
            "price": 1
        },
        status=200
    ) 
    
    posting_item = {
        "id": 1,
        "item_type": "PRODUCE",
        "name": "test_item",
        "posting_id": 1
    }
    responses.add( # Use to mock response from API
        responses.GET,
        "http://127.0.0.1:5007/getPosting", 
        json={"description": "test", "id": 1, "image": None, "posting_author": "test_author", "posting_item": posting_item , "quantity": 2, "user_id": 1 }, # response 
        status=200
    ) 
    
    
    responses.add( # Use to mock response from API
        responses.POST,
        "http://127.0.0.1:5007/removeStock", 
        status=200
    ) 
    
    responses.add( # Use to mock response from API
        responses.DELETE,
        "http://127.0.0.1:5008/flushCart", 
        status=200
    ) 

    responses.add( # Use to mock response from API
        responses.POST,
        "http://127.0.0.1:5009/addOrder", 
        status=200
    ) 
    
    response = client_controller.post('/createOrder', json={'userId': 1}) 
    assert response.status_code == 200
    data = response.json
    assert data['message'] == 'Sufficient stock'