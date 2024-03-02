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

        try: # check that role is in ROLE enum
            role = models.Role[role]
        except KeyError:
            return jsonify({'message': 'Invalid role.'})
        

        newUser = models.User(name, phoneNumber, emailAddress, password, role, profileBio, farmerPid)
        models.db.session.add(newUser)
        models.db.session.commit()
        
        return jsonify({'message': 'New user created!'}), 200

    def login(self):
        data = request.json
        emailAddress = data['email_address']
        password = data['password']
        user = models.User.query.filter_by(email_address=emailAddress, password=password).first()

        if user is None:
            return jsonify({'message': 'Invalid email address or password.'}), 401
        else:
            return jsonify({'message': 'Successful Login! The user\'s ID is ' + str(user.id), 'userId': user.id}), 200

userManagementService = UserManagementService()
main.route('/', methods=['GET'])(userManagementService.testing)
main.route('/register', methods=['POST'])(userManagementService.register)
main.route('/login', methods=['POST'])(userManagementService.login)