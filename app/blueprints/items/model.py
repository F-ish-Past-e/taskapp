from app import db
from datetime import datetime
from app.blueprints.tasks.model import Task
class Items(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	item_logged = db.Column(db.Integer)
	task_id = db.Column(db.Integer, db.ForeignKey('task.id'))
	tasks = db.relationship('Task', backref='items')
	item_descr = db.Column(db.String(500), nullable=False)
	item_start_date = db.Column(db.Date, default=datetime.utcnow)
	item_end_date = db.Column(db.Date, default=datetime.utcnow)
	item_completed = db.Column(db.Boolean, default=False)