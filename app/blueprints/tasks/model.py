from app import db
from datetime import datetime
from app.blueprints.task_categories.model import Categories

class Task(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	task_logged = db.Column(db.Integer)
	category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
	category = db.relationship('Categories', backref='tasks')
	task_descr = db.Column(db.String(500), nullable=False)
	task_start_date = db.Column(db.Date, default=datetime.utcnow)
	task_end_date = db.Column(db.Date, default=datetime.utcnow)
	task_completed = db.Column(db.Boolean, default=False)