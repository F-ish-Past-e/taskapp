from app import db
class Priority(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	pri_logged = db.Column(db.Integer)
	priority_descr = db.Column(db.String(150))
	priority_type = db.Column(db.String(100))
	color = db.Column(db.String(100))
