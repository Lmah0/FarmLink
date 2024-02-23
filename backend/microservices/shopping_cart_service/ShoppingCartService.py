from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import requests
import json
from flask import Blueprint
from . import IShoppingCartService

main = Blueprint('main', __name__)

class ShoppingCartService(IShoppingCartService.IShoppingCartService):
    def testing(self):
        return 'Hello, World! This is the Shopping Cart Service.'
    
    def addToCart(self):
        pass

    def removeFromCart(self):
        pass

    def returnCart(self):
        pass

    def flushCart(self):
        pass

shoppingCartService = ShoppingCartService()

main.route('/', methods=['GET'])(shoppingCartService.testing)
main.route('/addToCart', methods=['POST'])(shoppingCartService.addToCart)
main.route('/removeFromCart', methods=['DELETE'])(shoppingCartService.removeFromCart)
main.route('/returnCart', methods=['GET'])(shoppingCartService.returnCart)
main.route('/flushCart', methods=['DELETE'])(shoppingCartService.flushCart)