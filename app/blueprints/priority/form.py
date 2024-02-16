from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired

class PriorityAddForm(FlaskForm):
	add_pri_descr = StringField(validators=[DataRequired()])
	add_priority_type = SelectField(validators=[DataRequired()],
		choices=[('', '--select--'), ('tasks', 'Tasks'), ('items', 'Items')]
	)

	add_pri_submit = SubmitField( label='Save')

class PriorityEditForm(FlaskForm):
	edit_pri_descr = StringField(validators=[DataRequired()])
	edit_priority_type = SelectField(validators=[DataRequired()],
		choices=[('', '--select--'), ('tasks', 'Tasks'), ('items', 'Items')]
	)
	edit_pri_submit = SubmitField(label='Update')