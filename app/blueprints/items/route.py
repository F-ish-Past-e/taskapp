from flask import render_template, redirect, request, url_for, flash
from app.blueprints.items import items
from app.blueprints.items.form import ItemAddForm, ItemEditForm
from app.blueprints.items.model import Items
from app.blueprints.categories.model import Categories
from app.blueprints.priority.model import Priority
from datetime import datetime
from flask_login import current_user
from app import db

@items.route('/item_list', methods=['POST', ])
def item_list():
	clicked_task_row = request.form.get('clickedTaskRow')
	current_date = datetime.now()
	# partial list load
	if 'clickedStatus' in request.form:
		if request.form.get('clickedStatus') == 'pending':
			item_list_stmt = Items.query.filter(Items.task_id == clicked_task_row, Items.item_end_date >= current_date.date(), Items.item_completed == False).order_by(Items.item_start_date).all()
		elif request.form.get('clickedStatus') == 'outstanding':
			item_list_stmt = Items.query.filter(Items.task_id == clicked_task_row, Items.item_end_date < current_date.date(), Items.item_completed == False).order_by(Items.item_start_date).all()
		elif request.form.get('clickedStatus') == 'completed':
			item_list_stmt = Items.query.filter(Items.task_id == clicked_task_row, Items.item_completed == True).order_by(Items.item_start_date).all()
		else:
			item_list_stmt = Items.query.filter(Items.task_id == clicked_task_row).order_by(Items.item_start_date).all()
		itemArray = [
			(
				{
					'itemID':i.id,
					'itemDescr':i.item_descr,
					'itemSartDate':i.item_start_date,
					'itemEndDate':i.item_end_date,
					'itemComp':i.item_completed,
					'itemCat':i.category.cat_descr,
					'itemPri':i.priority.priority_descr,
				}
			) for i in item_list_stmt
		]
		return render_template('/tasks/itemList_partial.html', item_list_stmt=item_list_stmt, itemArray=itemArray, current_date=current_date)
	# initial list load
	item_list_stmt = Items.query.filter(Items.task_id == clicked_task_row, Items.item_end_date >= current_date.date(), Items.item_completed == False).order_by(Items.item_start_date).all()
	itemArray = [
		(
			{
				'itemID':i.id,
				'itemDescr':i.item_descr,
				'itemSartDate':i.item_start_date,
				'itemEndDate':i.item_end_date,
				'itemComp':i.item_completed,
				'itemCat':i.category.cat_descr,
				'itemPri':i.priority.priority_descr,
			}
		) for i in item_list_stmt
	]

	return render_template('/tasks/itemList.html', clicked_task_row=clicked_task_row, itemArray=itemArray)

@items.route('/item_add', methods=['POST', 'GET'])
def item_add():
	item_add_form = ItemAddForm()

	item_cat_stmt = Categories.query.filter(Categories.cat_logged==current_user.id, Categories.cat_type=='items').all()
	item_cat_choices = [('', '--select--')]
	item_cat_choices.extend([(a.id, a.cat_descr) for a in item_cat_stmt])
	item_add_form.add_item_category.choices = item_cat_choices

	item_pri_stmt = Priority.query.filter(Priority.pri_logged==current_user.id, Priority.priority_type=='items').all()
	item_pri_choices = [('', '--select--')]
	item_pri_choices.extend([(b.id, b.priority_descr) for b in item_pri_stmt])
	item_add_form.add_item_priority.choices = item_pri_choices

	if item_add_form.validate_on_submit():
		item_add_stmt = Items(
			task_id=request.form.get('hiddenTaskID'),
			item_logged=current_user.id,
			category_id=item_add_form.add_item_category.data,
			priority_id=item_add_form.add_item_priority.data,
			item_descr=item_add_form.add_item_descr.data,
			item_start_date=item_add_form.add_item_start_date.data,
			item_end_date=item_add_form.add_item_end_date.data,
			item_completed=False,
		)
		db.session.add(item_add_stmt)
		db.session.commit()
		return ''
	return render_template('/tasks/itemAdd.html', item_add_form=item_add_form, hiddenTaskID=request.form.get('hidden_task_id'))

@items.route('/item_edit', methods=['POST', 'GET'])
def item_edit():
	item_edit_form = ItemEditForm()
	edit_cat_stmt = Categories.query.filter(Categories.cat_logged==current_user.id, Categories.cat_type=='items').all()
	edit_cat_choices = [(e.id, e.cat_descr) for e in edit_cat_stmt]
	item_edit_form.edit_item_category.choices = edit_cat_choices

	edit_pri_stmt = Priority.query.filter(Priority.pri_logged==current_user.id, Priority.priority_type=='items').all()
	edit_pri_choices = [(d.id, d.priority_descr) for d in edit_pri_stmt]
	item_edit_form.edit_item_priority.choices = edit_pri_choices
	if 'clickItemRow' in request.form:
		item_edit_stmt = Items.query.get(request.form.get('clickItemRow'))
		hidden_item_id = item_edit_stmt.id
		item_edit_form.edit_item_descr.data = item_edit_stmt.item_descr
		item_edit_form.edit_item_start_date.data = item_edit_stmt.item_start_date
		item_edit_form.edit_item_end_date.data = item_edit_stmt.item_end_date
		item_edit_form.edit_item_category.data = str(item_edit_stmt.category_id)
		item_edit_form.edit_item_priority.data = str(item_edit_stmt.priority_id)
		item_edit_form.edit_item_completed.data = item_edit_stmt.item_completed
		return render_template('/tasks/itemEdit.html', item_edit_form=item_edit_form, hidden_item_id=hidden_item_id)
	if item_edit_form.validate_on_submit():
		item_edit_stmt = Items.query.get(request.form.get('hidden_item_id'))		
		item_edit_stmt.item_descr = item_edit_form.edit_item_descr.data
		item_edit_stmt.item_start_date = item_edit_form.edit_item_start_date.data
		item_edit_stmt.item_end_date = item_edit_form.edit_item_end_date.data
		item_edit_stmt.category_id = item_edit_form.edit_item_category.data
		item_edit_stmt.priority_id = item_edit_form.edit_item_priority.data
		item_edit_stmt.item_completed = item_edit_form.edit_item_completed.data
		db.session.commit()
		return ''

@items.route('/item_delete', methods=['POST', 'GET'])
def item_delete():
	item_del_stmt = Items.query.filter(Items.id==request.form.get('itemDeleteID')).delete()
	db.session.commit()
	return ''

@items.route('/item_delete_confirm', methods=['POST', 'GET'])
def item_delete_confirm():
	return render_template('/tasks/item_delete.html', itemID=request.form.get('itemDeleteID'))

