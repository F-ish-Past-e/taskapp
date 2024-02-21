from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, DateField, TextAreaField, IntegerField, SelectField
from wtforms.validators import DataRequired

class TaskAddForm(FlaskForm):
	add_task_category = SelectField(validators=[DataRequired()])
	add_task_priority = SelectField(validators=[DataRequired()])
	add_task_descr = TextAreaField(validators=[DataRequired()])
	add_task_start_date = DateField(validators=[DataRequired()])
	add_task_end_date = DateField(validators=[DataRequired()])

class TaskEditForm(FlaskForm):
	edit_task_category = SelectField(validators=[DataRequired()])
	edit_task_priority = SelectField(validators=[DataRequired()])
	edit_task_descr = TextAreaField(validators=[DataRequired()])
	edit_task_start_date = DateField(validators=[DataRequired()])
	edit_task_end_date = DateField(validators=[DataRequired()])
	edit_task_completed = BooleanField()

