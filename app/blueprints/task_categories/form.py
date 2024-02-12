from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, DateField, TextAreaField, IntegerField
from wtforms.validators import DataRequired

class catAddForm(FlaskForm):
	add_cat_descr = StringField(validators=[DataRequired()])

class catEditForm(FlaskForm):
	edit_cat_descr = StringField(validators=[DataRequired()])

