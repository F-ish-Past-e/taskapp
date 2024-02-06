from app import db
from datetime import datetime

class Categories(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	cat_descr = db.Column(db.String(100), nullable=False)
