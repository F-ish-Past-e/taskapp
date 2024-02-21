from app import db
from datetime import datetime
from app.blueprints.tasks.model import Task
from app.blueprints.categories.model import Categories
from app.blueprints.priority.model import Priority

class Items(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	item_logged = db.Column(db.Integer)
	task_id = db.Column(db.Integer, db.ForeignKey('task.id'))
	tasks = db.relationship('Task', backref='items')
	item_descr = db.Column(db.String(500), nullable=False)
	category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
	category = db.relationship('Categories', backref='item_tasks')
	priority_id = db.Column(db.Integer, db.ForeignKey('priority.id'))
	priority = db.relationship('Priority', backref='item_priorities')
	item_start_date = db.Column(db.Date, default=datetime.utcnow)
	item_end_date = db.Column(db.Date, default=datetime.utcnow)
	item_completed = db.Column(db.Boolean, default=False)