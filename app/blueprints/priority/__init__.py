from flask import Blueprint

priority = Blueprint('priority', __name__)

from app.blueprints.priority import route