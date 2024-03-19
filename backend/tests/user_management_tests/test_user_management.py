from microservices.user_management_service.models import User, Role
from microservices.user_management_service import db

# Tests for register
def test_register_with_invalid_role(client, app): # use client to send simulated requests to service
    data = {
        "name": "John Doe",
        "phone_number": "1234567890",
        "email_address": "test@gmail.com",
        "password": "password",
        "role": "INVALID",
        "farmer_pid": "1234567890",
        "profile_bio": "I am a farmer"
    }
    response = client.post('/register', json=data)
    assert response.status_code == 400
    assert b'Invalid role.' in response.data

def test_register_with_non_farmer_and_assigned_pid(client, app):
    data = {
        "name": "John Doe",
        "phone_number": "1234567890",
        "email_address": "test@gmail.com",
        "password": "password",
        "role": "NONFARMER",
        "farmer_pid": "1234567890",
        "profile_bio": "I am a farmer"
    }
    response = client.post('/register', json=data)
    assert response.status_code == 400
    assert b'Farmer PID is not required for non-farmers.' in response.data

def test_register_with_farmer_and_no_pid(client, app):
    data = {
        "name": "John Doe",
        "phone_number": "1234567890",
        "email_address": "test@gmail.com",
        "password": "password",
        "role": "FARMER",
        "farmer_pid": None,
        "profile_bio": "I am a farmer"
    }
    response = client.post('/register', json=data)
    assert response.status_code == 400
    assert b'Farmer PID is required for farmers.' in response.data

# Tests for login
def test_login_with_invalid_email(client, app):
    data = {
        "email_address": None,
        "password": "password"
    }
    response = client.post('/login', json=data)
    assert response.status_code == 400
    assert b'Email address and password are required.' in response.data

def test_login_with_invalid_password(client, app):
    data = {
        "email_address": "test@gmail.com",
        "password": None
    }
    response = client.post('/login', json=data)
    assert response.status_code == 400
    assert b'Email address and password are required.' in response.data

def test_login_with_incorrect_email(client, app):
    with app.app_context():
        test_user = User(
            name="John Doe",
            phoneNumber="1234567890",
            emailAddress="test@gmail.com",
            password="password",
            role=Role.FARMER,
            farmer_pid="1234567890",
            profileBio="I am a farmer"
        )
        db.session.add(test_user)
        db.session.commit()
    data = {
        "email_address": "wrong@gmail.com",
        "password": "password"
    }
    response = client.post('/login', json=data)
    assert response.status_code == 401
    assert b'Invalid email address or password.' in response.data

def test_login_with_incorrect_password(client, app):
    with app.app_context():
        test_user = User(
            name="John Doe",
            phoneNumber="1234567890",
            emailAddress="test@gmail.com",
            password="password",
            role=Role.FARMER,
            farmer_pid="1234567890",
            profileBio="I am a farmer"
        )
        db.session.add(test_user)
        db.session.commit()
    data = {
        "email_address": "test@gmail.com",
        "password": "wrong"
    }
    response = client.post('/login', json=data)
    assert response.status_code == 401
    assert b'Invalid email address or password.' in response.data

        

