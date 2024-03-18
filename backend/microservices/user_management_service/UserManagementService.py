from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import requests
import json
from flask import Blueprint
from . import IUserManagementService, models

main = Blueprint('main', __name__)


class UserManagementService(IUserManagementService.IUserManagementService):
    def testing(self):
        return 'Hello, World! This is the User Management Service.'
    
    def register(self):
        data = request.json
        name = data['name']
        phoneNumber =  data['phone_number']
        emailAddress = data['email_address']
        password = data['password']
        role = data['role']
        farmerPid = data['farmer_pid']
        profileBio = data['profile_bio']

        if not name or not phoneNumber or not emailAddress or not password or role == None:
            return jsonify({'message': 'name, phone number, email address, password and role are required.'}), 400
        try: # check that role is in ROLE enum
            role = models.Role[role]
        except KeyError:
            return jsonify({'message': 'Invalid role.'}), 400
        
        if role == models.Role.FARMER and not farmerPid:
            return jsonify({'message': 'Farmer PID is required for farmers.'}), 400
        elif role == models.Role.NONFARMER and farmerPid:
            return jsonify({'message': 'Farmer PID is not required for non-farmers.'}), 400
        
        

        newUser = models.User(name, phoneNumber, emailAddress, password, role, profileBio, farmerPid)
        models.db.session.add(newUser)
        models.db.session.commit()
        
        return jsonify({'message': 'New user created!'}), 200

    def login(self):
        data = request.json
        emailAddress = data['email_address']
        password = data['password']
        user = models.User.query.filter_by(email_address=emailAddress, password=password).first()

        if not emailAddress or not password:
            return jsonify({'message': 'Email address and password are required.'}), 400

        if user is None:
            return jsonify({'message': 'Invalid email address or password.'}), 401
        else:
            return jsonify({'message': 'Successful Login! The user\'s ID is ' + str(user.id), 'userId': user.id}), 200
    
    def returnProfile(self):
        data = request.json
        userId = data['userId']
        user = models.User.query.filter_by(id=userId).first()
        
        if user is None:
            return jsonify({'message': 'Invalid user ID.'}), 401
        else:
            return jsonify(user.serialize()), 200

userManagementService = UserManagementService()
main.route('/', methods=['GET'])(userManagementService.testing)
main.route('/register', methods=['POST'])(userManagementService.register)
main.route('/login', methods=['POST'])(userManagementService.login)
main.route('/returnProfile', methods=['POST'])(userManagementService.returnProfile)