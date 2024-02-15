// loading the category list into the bootstrap modal dialog div content
$('.categoiresClick').click(function(){
	$.post('/task_category_list', function(cat_data_list){
		$('.contentDiv').html(cat_data_list)
		$('#category_modal_list').modal('show')
	})
})

// displaying the edit content for task categories
$(document).on('click', '#catTbodyID tr', function(){
	clickedCatEditRow = $(this).attr('id')
	$('#category_modal_list').modal('hide')
	$.post('/task_category_edit', {clickedCatEditRow:clickedCatEditRow}, function(cat_data_edit){
		$('.contentDiv').html(cat_data_edit)
		$('#category_modal_edit').modal('show')
	})
})

// displaying the task categories add html
$(document).on('click', '#task_category_add_button', function(){
	$('#category_modal_list').modal('hide')
	$.post('task_category_add', function(task_category_add_return){
		$('.contentDiv').html(task_category_add_return)
		$('#category_modal_add').modal('show')
	})
})

// Saving the task category
$(document).on('submit', '#taskCatAddForm', function(event){
	event.preventDefault()
	$.post('task_category_add', $('#taskCatAddForm').serialize(), function(){
		$('#category_modal_add').modal('hide')	
		// ajax to load the task category list again
		$.post('task_category_list', function(new_cat_data_list){
			$('.contentDiv').html(new_cat_data_list)
			$('#category_modal_list').modal('show')
		})
	})
})

// Editing the task category
$(document).on('submit', '#taskCatEditForm', function(event){
	event.preventDefault()
	$.post('task_category_edit', $('#taskCatEditForm').serialize(), function(){
		$('#category_modal_edit').modal('hide')	
		// ajax to load the task category list again
		$.post('task_category_list', function(new_cat_data_list){
			$('.contentDiv').html(new_cat_data_list)
			$('#category_modal_list').modal('show')
		})
	})
})

$(document).on('click', '.cat_add_back_but', function(){
	$('#category_modal_add').modal('hide')
	$.post('task_category_list', function(new_cat_data_list){
		$('.contentDiv').html(new_cat_data_list)
		$('#category_modal_list').modal('show')	
	})
})

$(document).on('click', '.cat_edit_back_but', function(){
	$('#category_modal_edit').modal('hide')
	$.post('task_category_list', function(new_cat_data_list){
		$('.contentDiv').html(new_cat_data_list)
		$('#category_modal_list').modal('show')	
	})
})
