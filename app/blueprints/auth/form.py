from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
	username = StringField(validators=[DataRequired()])
	password = PasswordField(validators=[
		DataRequired(),
		Length(min=8),
	])
	submit = SubmitField()

class RegisterForm(FlaskForm):
	username = StringField(validators=[DataRequired()])
	password = PasswordField(
		validators=[
			DataRequired(),
			Length(min=8),
		]
	)
	confirm_password = PasswordField(
		validators=[
			DataRequired(),
			Length(min=8),
		]
	)
	submit = SubmitField()

class UserEditForm(FlaskForm):
	username = StringField(validators=[DataRequired()])
	submit = SubmitField()
