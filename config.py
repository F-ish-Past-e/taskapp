import os
class Config(object):
	APP_NAME='Task App'
	SECRET_KEY = os.urandom(24)
	SQLALCHEMY_DATABASE_URI = "mariadb+pymysql://the_db_username:the_db_password@localhost/the_db_you_created"