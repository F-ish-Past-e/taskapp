import os
class Config(object):
	FLASK_APP='app:create_app'
	FLASK_DEBUG=os.getenv('FLASK_DEBUG', False)
	APP_NAME='Task App'
	SECRET_KEY=os.getenv("SECRET_KEY", os.urandom(24))
	SQLALCHEMY_DATABASE_URI=os.getenv('SQLALCHEMY_DATABASE_URI', 'sqlite:///task_app.db')
