from app import db
from datetime import datetime
from app.blueprints.categories.model import Categories
from app.blueprints.priority.model import Priority

class Task(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	task_logged = db.Column(db.Integer)
	category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
	category = db.relationship('Categories', backref='tasks')
	priority_id = db.Column(db.Integer, db.ForeignKey('priority.id'))
	priority = db.relationship('Priority', backref='priorities')
	task_descr = db.Column(db.String(500), nullable=False)
	task_start_date = db.Column(db.Date, default=datetime.utcnow)
	task_end_date = db.Column(db.Date, default=datetime.utcnow)
	task_completed = db.Column(db.Boolean, default=False)