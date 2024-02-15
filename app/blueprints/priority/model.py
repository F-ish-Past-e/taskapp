from app import db
class Priority(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	pri_logged = db.Column(db.Integer)
	priority_descr = db.Column(db.String(150))
	color = db.Column(db.String(100))
