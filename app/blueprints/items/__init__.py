from flask import Blueprint

items = Blueprint('items', __name__)

from app.blueprints.items import route