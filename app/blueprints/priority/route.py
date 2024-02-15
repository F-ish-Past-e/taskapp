from app.blueprints.priority import priority
from app.blueprints.priority.model import Priority
from app.blueprints.priority.form import PriorityAddForm, PriorityEditForm
from flask import render_template, redirect, request, url_for, flash

@priority.route('/priority_list', methods=['POST', 'GET'])
def priority_list():
	return render_template('task_priorities/task_pri_list.html')

@priority.route('/priority_add', methods=['POST', 'GET'])
def priority_add():
	return 'something'

@priority.route('/priority_edit', methods=['POST', 'GET'])
def priority_edit():
	return 'something'