// loading the category list into the bootstrap modal dialog div content
$('.categoiresClick').click(function(){
	$.post('/task_category_list', function(cat_data_list){
		$('.category_contentdiv_list').html(cat_data_list)
		$('#category_modal_list').modal('show')
	})
})

// displaying the edit content for task categories
$(document).on('click', '#catTbodyID tr', function(){
	clickedCatEditRow = $(this).attr('id')
	$.post('/task_category_edit', {clickedCatEditRow:clickedCatEditRow}, function(cat_data_edit){
		$('.category_contentdiv_edit').html(cat_data_edit)
		$('#category_modal_list').modal('hide')
		$('#category_modal_edit').modal('show')
	})
})

// displaying the task categories add html
$(document).on('click', '#task_category_add_button', function(){
	$.post('task_category_add', function(task_category_add_return){
		$('.category_contentdiv_add').html(task_category_add_return)
		$('#category_modal_list').modal('hide')
		$('#category_modal_add').modal('show')
	})
})

// Saving the task category
$(document).on('submit', '#taskCatAddForm', function(event){
	event.preventDefault()
	$.post('task_category_add', $('#taskCatAddForm').serialize(), function(){
		// ajax to load the task category list again
		$.post('task_category_list', function(new_cat_data_list){
			$('.category_contentdiv_list').html(new_cat_data_list)
			$('#category_modal_add').modal('hide')	
			$('#category_modal_list').modal('show')
		})
	})
})

// Editing the task category
$(document).on('submit', '#taskCatEditForm', function(event){
	event.preventDefault()
	$.post('task_category_edit', $('#taskCatEditForm').serialize(), function(){
		// ajax to load the task category list again
		$.post('task_category_list', function(new_cat_data_list){
			$('.category_contentdiv_list').html(new_cat_data_list)
			$('#category_modal_edit').modal('hide')	
			$('#category_modal_list').modal('show')
		})
	})
})
