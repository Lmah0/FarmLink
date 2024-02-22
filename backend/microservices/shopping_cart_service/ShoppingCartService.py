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

shoppingCartService = ShoppingCartService()

main.route('/', methods=['GET'])(shoppingCartService.testing)