from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, DateField, TextAreaField, IntegerField, SelectField
from wtforms.validators import DataRequired

class PriorityAddForm(FlaskForm):
	add_priority_category = SelectField(coerce=int, validators=[DataRequired()])

class PriorityEditForm(FlaskForm):
	edit_priority_category = SelectField(coerce=int, validators=[DataRequired()])
