from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, DateField, TextAreaField, IntegerField
from wtforms.validators import DataRequired

class CatAddForm(FlaskForm):
	add_cat_descr = StringField(validators=[DataRequired()])

class CatEditForm(FlaskForm):
	edit_cat_descr = StringField(validators=[DataRequired()])

