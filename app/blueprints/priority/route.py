from app.blueprints.priority import priority
from app.blueprints.priority.model import Priority
from app.blueprints.priority.form import PriorityAddForm, PriorityEditForm
from flask import render_template, redirect, request, url_for, flash
from flask_login import current_user
from app import db

@priority.route('/priority_list', methods=['POST', 'GET'])
def priority_list():
	hid_Pri_type = request.form.get('hidden_pri_type')
	pri_list_stmt = Priority.query.filter(Priority.pri_logged==current_user.id, Priority.priority_type==hid_Pri_type).all()
	pri_list_obj = [
		(
			{
				'PriID':a.id,
				'PriDescr':a.priority_descr,
				'PriColor':a.color,
				'PriType': 'Tasks' if a.priority_type == 'tasks' else 'Items' if a.priority_type == 'items' else None,
			}
		) for a in pri_list_stmt]
	return render_template('/priorities/pri_list.html', pri_list_obj=pri_list_obj, hid_Pri_type=hid_Pri_type)

@priority.route('/priority_add', methods=['POST', 'GET'])
def priority_add():
	pri_add_form = PriorityAddForm()
	hidPriType = request.form.get('hidPriType')
	if pri_add_form.validate_on_submit():
		pri_add_stmt = Priority(
			pri_logged=current_user.id,
			priority_descr=pri_add_form.add_pri_descr.data,
			priority_type=request.form.get('hiddenPriType'),
			color=request.form.get('hiddenSelectedColor')
		)
		db.session.add(pri_add_stmt)
		db.session.commit()
		return ''
	return render_template('priorities/pri_add.html', pri_add_form=pri_add_form, hidPriType=hidPriType)

@priority.route('/priority_edit', methods=['POST', 'GET'])
def priority_edit():
	pri_edit_form = PriorityEditForm()
	pri_edit_stmt = Priority.query.get(request.form.get('clickedPriRow'))
	if pri_edit_form.validate_on_submit():
		pri_edit_stmt = Priority.query.get(request.form.get('hiddenPriEditID'))
		pri_edit_stmt.priority_descr = pri_edit_form.edit_pri_descr.data
		pri_edit_stmt.color = request.form.get('PriSelectedColor')
		db.session.commit()
		return ''
	pri_edit_form.edit_pri_descr.data = pri_edit_stmt.priority_descr
	pri_selected_color = pri_edit_stmt.color
	return render_template('priorities/pri_edit.html', pri_edit_form=pri_edit_form, clickedPriRow=request.form.get('clickedPriRow'), pri_selected_color=pri_selected_color)