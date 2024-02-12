from flask import Blueprint

task_categories = Blueprint('task_categories', __name__)

from app.blueprints.task_categories import route