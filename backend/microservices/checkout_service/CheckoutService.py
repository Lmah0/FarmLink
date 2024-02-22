from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import requests
import json
from flask import Blueprint
from . import ICheckoutService

main = Blueprint('main', __name__)

class CheckoutService(ICheckoutService.ICheckoutService):
    def testing(self):
        return 'Hello, World! This is the Checkout Service.'

checkoutService = CheckoutService()

main.route('/', methods=['GET'])(checkoutService.testing)