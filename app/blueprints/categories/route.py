from flask import render_template, redirect, url_for, request, flash
from app.blueprints.categories.model import Categories
from app.blueprints.categories.form import CatAddForm, CatEditForm
from app.blueprints.categories import categories
from flask_login import login_required, current_user
from app import db

# populating the task category list
@categories.route('/category_list', methods=['POST', 'GET'])
@login_required
def category_list():
	hidden_cat = request.form.get('hidden_cat')
	cat_list_array = []
	cat_list_stmt = Categories.query.filter(Categories.cat_logged==current_user.id, Categories.cat_type==hidden_cat).all()
	for cat_list in cat_list_stmt:
		cat_list_obj = {
			'cat_id':cat_list.id,
			'cat_descr':cat_list.cat_descr,
		}
		cat_list_array.append(cat_list_obj)

	return render_template('/categories/category_list.html', cat_list=cat_list_array, hidden_cat=hidden_cat)

# add for the task categories
@categories.route('/category_add', methods=['POST', 'GET'])
@login_required
def category_add():
	cat_add_form = CatAddForm()
	hidCat = request.form.get('hidCat')
	if cat_add_form.validate_on_submit():
		cat_add = Categories(
			cat_descr=cat_add_form.add_cat_descr.data,
			cat_type=request.form.get('hidCat'),
			cat_logged=current_user.id,
		)
		db.session.add(cat_add)
		db.session.commit()
		return redirect(url_for('categories.category_list'))
	return render_template('/categories/category_add.html', cat_add_form=cat_add_form, hidCat=hidCat)

# displaying the edit and updating the task categories
@categories.route('/category_edit', methods=['POST', 'GET'])
@login_required
def category_edit():
	cat_edit_form = CatEditForm()
	hiddenCat = request.form.get('hiddenCat')
	if cat_edit_form.validate_on_submit():
		cat_edit_stmt = Categories.query.get(request.form.get('clickedCatEditRow'))
		cat_edit_stmt.cat_descr = cat_edit_form.edit_cat_descr.data
		db.session.commit()
		return redirect(url_for('categories.category_list'))
	cat_edit_stmt = Categories.query.get(request.form.get('clickedCatEditRow'))
	cat_edit_form.edit_cat_descr.data = cat_edit_stmt.cat_descr
	return render_template('/categories/category_edit.html', cat_edit_form=cat_edit_form, clickedCatEditRow=request.form.get('clickedCatEditRow'), hiddenCat=hiddenCat)

@categories.route('/catDelete', methods=['POST', 'GET'])
@login_required
def catDelete():
	if request.form.get('hiddenCat')=='tasks':
		from app.blueprints.tasks.model import Task
		task_check_stmt = Task.query.filter(Task.category_id==request.form.get('catDeleteID')).all()
		if task_check_stmt:
			return 'outstanding_records'
		else:
			Categories.query.filter(Categories.id==request.form.get('catDeleteID')).delete()
			db.session.commit()
			return ''
	if request.form.get('hiddenCat')=='items':
		from app.blueprints.items.model import Items
		item_check_stmt = Items.query.filter(Items.category_id==request.form.get('catDeleteID')).all()
		if item_check_stmt:
			return 'outstanding_records'
		else:
			Categories.query.filter(Categories.id==request.form.get('catDeleteID')).delete()
			db.session.commit()
			return ''

@categories.route('/catDeleteConfirm', methods=['POST'])
@login_required
def deleteConfirm():
	return render_template('categories/cat_delete.html', clickedCatEditRow=request.form.get('catDeleteID'), hiddenCat=request.form.get('hiddenCat'))
