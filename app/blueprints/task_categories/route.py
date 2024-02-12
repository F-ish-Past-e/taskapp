from flask import render_template, redirect, url_for, request, flash
from app.blueprints.task_categories.model import Categories
from app.blueprints.task_categories.form import catAddForm, catEditForm
from app.blueprints.task_categories import task_categories
from flask_login import login_required
from app import db

@task_categories.route('/task_category_list', methods=['POST', 'GET'])
@login_required
def category_list():
	cat_list_array = []
	cat_list_stmt = Categories.query.all()
	for cat_list in cat_list_stmt:
		cat_list_obj = {
			'cat_id':cat_list.id,
			'cat_descr':cat_list.cat_descr,
		}
		cat_list_array.append(cat_list_obj)

	return render_template('/task_categories/category_list.html', cat_list=cat_list_array)

@task_categories.route('/task_category_add', methods=['POST', 'GET'])
def category_add():
	cat_add_form = catAddForm()
	if cat_add_form.validate_on_submit():
		cat_add = Categories(cat_descr=cat_add_form.add_cat_descr.data)
		db.session.add(cat_add)
		db.session.commit()
		return redirect(url_for('task_categories.category_list'))
	return render_template('/task_categories/category_add.html', cat_add_form=cat_add_form)

@task_categories.route('/task_category_edit', methods=['POST', 'GET'])
def category_edit():
	cat_edit_form = catEditForm()
	if cat_edit_form.validate_on_submit():
		cat_edit_stmt = Categories.query.get(request.form.get('clickedCatEditRow'))
		cat_edit_stmt.cat_descr = cat_edit_form.edit_cat_descr.data
		db.session.commit()
		return redirect(url_for('task_categories.category_list'))
	cat_edit_stmt = Categories.query.get(request.form.get('clickedCatEditRow'))
	cat_edit_form.edit_cat_descr.data = cat_edit_stmt.cat_descr
	return render_template('/task_categories/category_edit.html', cat_edit_form=cat_edit_form, clickedCatEditRow=request.form.get('clickedCatEditRow'))
