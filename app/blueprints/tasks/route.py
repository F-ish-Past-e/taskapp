from flask import render_template, request, redirect, jsonify
from app.blueprints.tasks import tasks
from app.blueprints.tasks.model import Task
from app.blueprints.task_categories.model import Categories
from app.blueprints.tasks.form import TaskAddForm, TaskEditForm
from flask_login import login_required, current_user
from datetime import datetime
from app import db

@tasks.route('/tasksList', methods=['GET', 'POST'])
@login_required
def tasksList():
	current_date = datetime.now()
	if request.method == 'POST':
		clickedStatus = request.form['clickedStatus']
		if clickedStatus == 'completed':
			taskListSTMT = Task.query.filter(Task.task_logged==current_user.id, Task.task_completed == True).all()
		elif clickedStatus == 'pending':
			taskListSTMT = Task.query.filter(Task.task_logged==current_user.id, Task.task_end_date >= current_date.date(), Task.task_completed == False).all()
		elif clickedStatus == 'outstanding':
			taskListSTMT = Task.query.filter(Task.task_logged==current_user.id, Task.task_end_date < current_date.date(), Task.task_completed == False).all()
		else:
			taskListSTMT = Task.query.filter(Task.task_logged==current_user.id)

		task_list_array = []
		for t_list in taskListSTMT:
			task_data = {
				'taskID': t_list.id,
				'taskDescr': t_list.task_descr,
				'taskStartdate': t_list.task_start_date,
				'taskEnddate': t_list.task_end_date,
				'taskCategory': t_list.category.cat_descr,
				'taskCompleted': t_list.task_completed,
			}
			task_list_array.append(task_data)

		return render_template('tasks/taskList_partial.html', task_list=task_list_array, current_date=current_date)

	taskListSTMT = Task.query.filter(Task.task_logged==current_user.id, Task.task_end_date >= current_date.date(), Task.task_completed == False).all()
	task_list_array = []
	for t_list in taskListSTMT:
		task_data = {
			'taskID': t_list.id,
			'taskDescr': t_list.task_descr,
			'taskStartdate': t_list.task_start_date,
			'taskEnddate': t_list.task_end_date,
			'taskCategory': t_list.category.cat_descr,
			'taskCompleted': t_list.task_completed,
		}
		task_list_array.append(task_data)
	return render_template('tasks/taskList.html', task_list=task_list_array, current_date=current_date)

@tasks.route('/taskAdd', methods=['GET', 'POST'])
@login_required
def taskAdd():
	task_add_form = TaskAddForm()
	if request.method == 'POST':
		if task_add_form.validate_on_submit:

			task_description = task_add_form.add_task_descr.data
			task_start_date = task_add_form.add_task_start_date.data
			task_end_date = task_add_form.add_task_end_date.data

			task_add_query = Task(
				task_logged = current_user.id,
				task_descr=task_description,
				task_start_date=task_start_date,
				task_end_date=task_end_date,
				category_id=task_add_form.add_task_category.data,
				task_completed=False,
			)
			db.session.add(task_add_query)
			db.session.commit()

		taskListSTMT = Task.query.all()
		return redirect('/tasksList')

	cat_stmt = Categories.query.filter(Categories.cat_logged==current_user.id).all()
	choices = [(cat.id, cat.cat_descr) for cat in cat_stmt]
	task_add_form.add_task_category.choices = choices

	return render_template('tasks/taskAdd.html', task_add_form=task_add_form)

# task edit page
@tasks.route('/taskEdit/', methods=['GET', 'POST'])
def taskEdit():

	task_edit_form = TaskEditForm()
	selectTask = Task.query.filter_by(id=request.form.get('clickedTaskRow')).first()

	edit_cat_stmt = Categories.query.filter(Categories.cat_logged==current_user.id).all()
	choices = [(edit_cat.id, edit_cat.cat_descr) for edit_cat in edit_cat_stmt]
	task_edit_form.edit_task_category.choices = choices

	task_edit_form.edit_task_category.data = selectTask.category_id
	task_edit_form.edit_task_descr.data = selectTask.task_descr
	task_edit_form.edit_task_start_date.data = selectTask.task_start_date
	task_edit_form.edit_task_end_date.data = selectTask.task_end_date
	task_edit_form.edit_task_completed.data = selectTask.task_completed
	
	return render_template('tasks/taskEdit.html', task_edit_form=task_edit_form, selectTask=selectTask)

# task update route
@tasks.route('/taskUpdate/<taskUpdateID>', methods=['GET', 'POST'])
@login_required
def taskUpdate(taskUpdateID):
	task_edit_form = TaskEditForm()
	taskUpdateSTMT = Task.query.filter_by(id=taskUpdateID).first()
	taskUpdateSTMT.task_descr = task_edit_form.edit_task_descr.data
	taskUpdateSTMT.task_start_date = task_edit_form.edit_task_start_date.data
	taskUpdateSTMT.task_end_date = task_edit_form.edit_task_end_date.data
	taskUpdateSTMT.task_completed = task_edit_form.edit_task_completed.data
	taskUpdateSTMT.category_id = task_edit_form.edit_task_category.data
	db.session.commit()
	return redirect('/tasksList')

# tasl delete route
@tasks.route('/taskDelete/<deletedID>', methods=['GET', 'POST'])
@login_required
def taskDelete(deletedID):
	Task.query.filter_by(id=deletedID).delete()
	db.session.commit()
	return redirect('/tasksList')

@tasks.route('/divsPage/<clickedTaskRow>')
def divsPage(clickedTaskRow):
	return render_template('/tasks/divs.html', clickedTaskRow=clickedTaskRow)



@tasks.route('/testing', methods=['POST', 'GET'])
def testing():
	return str(current_user.id)