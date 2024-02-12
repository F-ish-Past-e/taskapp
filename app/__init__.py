from flask import Flask, render_template, redirect, url_for, flash
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)

from app.blueprints.tasks import tasks as tasks_bp
app.register_blueprint(tasks_bp)

from app.blueprints.auth import auth as auth_bp
app.register_blueprint(auth_bp)

from app.blueprints.task_categories import task_categories as task_categories_bp
app.register_blueprint(task_categories_bp)

from app.blueprints.items import items as items_bp
app.register_blueprint(items_bp)

def create_app():

	@app.route('/')
	def index():
		return redirect(url_for('auth.login'))
	return app