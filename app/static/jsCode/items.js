// js for the settings of the items
$(document).off('click', '.item-dropdown-button').on('click', '.item-dropdown-button', function(){
	var dropdownContent = $(this).next(".dropdown-content");
	dropdownContent.toggle('fast');
})
// displaying the item add html
$(document).on('click', '#add_item_but', function(){
	hidden_task_id = $('#hiddenTaskID').val()
	$.post('/item_add', {hidden_task_id:hidden_task_id}, function(itemaddreturn){
		$('.contentDiv').html(itemaddreturn)
		$('#AddItemModal').modal('show')
	})
})
// saving the items
$(document).off('submit', '#itemAddForm').on('submit', '#itemAddForm', function(event){
	event.preventDefault()
	$.post('/item_add', $('#itemAddForm').serialize(), function(){
		$('#AddItemModal').modal('hide')
		window.location.reload()
	})
})
// click event for specific item
$(document).on('click', '#myTbodyID tr', function(){
	clickItemRow = $(this).attr('id')
	$.post('/item_edit', {clickItemRow:clickItemRow}, function(itemEditReturn){
		$('.contentDiv').html(itemEditReturn)
		$('#EditItemModal').modal('show')
	})
})

$(document).off('submit', '#itemEditForm').on('submit', '#itemEditForm', function(event){
	event.preventDefault()
	$.post('/item_edit', $('#itemEditForm').serialize(), function(){
		$('#EditItemModal').modal('hide')
		window.location.reload()
	})
})
$('#itemStatus').change(function(){
	clickedStatus = $(this).val()
	clickedTaskRow = $('#hiddenTaskID').val()
	$.post('/item_list', {clickedStatus:clickedStatus, clickedTaskRow:clickedTaskRow}, function(itemListData){
		$('#myTbodyID').html(itemListData)
	})
})

// trigger to display confirm html
$(document).off('click', '.deleteItemBut').on('click', '.deleteItemBut', function(){
	$('#EditItemModal').modal('hide')
	$.post('/item_delete_confirm', {itemDeleteID:$('#hidden_item_id').val()}, function(returnDelConfirm){
		$('.contentDiv').html(returnDelConfirm)
		$('#itemCheckDeleteModal').modal('show')
	})
})

// deleting category
$(document).off('click', '.itemDelConfirmBut').on('click', '.itemDelConfirmBut', function(){
	$.post('/item_delete', {itemDeleteID:$('#hiddenItemID').val()}, function(checkTasks){
		$('#itemCheckDeleteModal').modal('hide')
		window.location.reload()
	})
})

// back button from category delete
$(document).off('click', '.itemDelConfirmBack').on('click', '.itemDelConfirmBack', function(){
	$('#catCheckDeleteModal').modal('hide')
	$.post('/category_edit', {clickedCatEditRow:$('#clickedCatEditRow').val(), hiddenCat:$('#hiddenCat').val()}, function(new_cat_data_list){
		$('.contentDiv').html(new_cat_data_list)
		$('#category_modal_edit').modal('show')	
	})
})