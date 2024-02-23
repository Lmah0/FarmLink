from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import requests
import json
from flask import Blueprint
from . import IUserManagementService

main = Blueprint('main', __name__)


class UserManagementService(IUserManagementService.IUserManagementService):
    def testing(self):
        return 'Hello, World! This is the User Management Service.'
    
    def register(self):
        data = request.json
        userId = data["id"]
        name = data['name']
        phoneNumber =  data['phone_number']
        emailAddress = data['email_address']
        password = data['password']
        role = data['role']
        farmerPid = data['farmer_pid']
        profileBio = data['profile_bio']


        
        return jsonify({'message': 'New user created!'}), 200

    def login(self):
        pass

userManagementService = UserManagementService()
main.route('/', methods=['GET'])(userManagementService.testing)
main.route('/register', methods=['POST'])(userManagementService.register)
main.route('/login', methods=['POST'])(userManagementService.login)