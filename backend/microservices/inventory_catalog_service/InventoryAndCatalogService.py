from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import requests
import json
from flask import Blueprint
from . import IInventoryAndCatalogService

main = Blueprint('main', __name__)


class InventoryAndCatalogService(IInventoryAndCatalogService.IInventoryAndCatalogService):
    def testing(self):
        return 'Hello, World! This is the Inventory and Catalog Service.'

inventoryAndCatalogService = InventoryAndCatalogService()

main.route('/', methods=['GET'])(inventoryAndCatalogService.testing)

