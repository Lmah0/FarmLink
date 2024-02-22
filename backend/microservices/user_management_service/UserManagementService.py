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

userManagementService = UserManagementService()
main.route('/', methods=['GET'])(userManagementService.testing)