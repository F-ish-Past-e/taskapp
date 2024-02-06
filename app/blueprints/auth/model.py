from app import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64))
	password = db.Column(db.String(200))

# Check function to see if user already exists
def is_user_unique(username):
	return User.query.filter_by(username=username).count() == 0
