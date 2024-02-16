import os
class Config(object):
	APP_NAME='Task App'
	SECRET_KEY = os.urandom(24)
	SQLALCHEMY_DATABASE_URI = 'sqlite:///task_app.db'
