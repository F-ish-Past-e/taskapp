from flask import Flask, render_template, redirect, url_for, flash
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()

def create_app():

	app = Flask(__name__)
	app.config.from_object(Config)

	db.init_app(app)
	migrate.init_app(app, db)
	login.init_app(app)

	from app.blueprints.tasks import tasks as tasks_bp
	app.register_blueprint(tasks_bp)

	from app.blueprints.auth import auth as auth_bp
	app.register_blueprint(auth_bp)

	from app.blueprints.categories import categories as categories_bp
	app.register_blueprint(categories_bp)

	from app.blueprints.items import items as items_bp
	app.register_blueprint(items_bp)

	from app.blueprints.priority import priority as priority_bp
	app.register_blueprint(priority_bp)

	@app.route('/')
	def index():
		return redirect(url_for('auth.login'))
	return app