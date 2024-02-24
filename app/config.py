import os
class Config(object):
	APP_NAME='Task App'
	FLASK_APP='app:create_app'
	FLASK_DEBUG=os.getenv('FLASK_DEBUG', False)
	SECRET_KEY=os.getenv("SECRET_KEY", os.urandom(24))
	SQLALCHEMY_DATABASE_URI=os.getenv('SQLALCHEMY_DATABASE_URI', 'sqlite:///task_app.db')
