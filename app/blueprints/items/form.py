from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, DateField, TextAreaField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired

class ItemAddForm(FlaskForm):
	add_item_category = SelectField(validators=[DataRequired()])
	add_item_priority = SelectField(validators=[DataRequired()])
	add_item_descr = StringField(validators=[DataRequired()])
	add_item_start_date = DateField(validators=[DataRequired()])
	add_item_end_date = DateField(validators=[DataRequired()])
	add_item_submit = SubmitField('Commit')

class ItemEditForm(FlaskForm):
	edit_item_category = SelectField(validators=[DataRequired()])
	edit_item_priority = SelectField(validators=[DataRequired()])	
	edit_item_descr = StringField(validators=[DataRequired()])
	edit_item_start_date = DateField(validators=[DataRequired()])
	edit_item_end_date = DateField(validators=[DataRequired()])
	edit_item_completed = BooleanField()
	edit_item_submit = SubmitField('Commit')


