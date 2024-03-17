from microservices.checkout_service.models import Order
import responses 
@responses.activate
def test_controller(client, app): # use client to send simulated requests to service
    responses.add # Use to mock response from API

    
        
