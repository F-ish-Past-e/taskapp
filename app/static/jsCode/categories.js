// loading the category list into the bootstrap modal dialog div content
$('.categoiresClick').click(function(){
	hidden_cat = $('#hiddenCat').val()
	$.post('/category_list', {hidden_cat:hidden_cat}, function(cat_data_list){
		$('.contentDiv').html(cat_data_list)
		$('#category_modal_list').modal('show')
	})
})

// displaying the edit content for categories
$(document).on('click', '#catTbodyID tr', function(){
	clickedCatEditRow = $(this).attr('id')
	$('#category_modal_list').modal('hide')
	$.post('/category_edit', {clickedCatEditRow:clickedCatEditRow, hiddenCat:$('#hidCat').val()}, function(cat_data_edit){
		$('.contentDiv').html(cat_data_edit)
		$('#category_modal_edit').modal('show')
	})
})

// displaying the categories add html
$(document).on('click', '#category_add_button', function(){
	$('#category_modal_list').modal('hide')
	hidCat = $('#hidCat').val()
	$.post('/category_add', {hidCat:hidCat}, function(category_add_return){
		$('.contentDiv').html(category_add_return)
		$('#category_modal_add').modal('show')
	})
})

// Saving the category
$(document).on('submit', '#catAddForm', function(event){
	event.preventDefault()
	$.post('/category_add', $('#catAddForm').serialize(), function(){
		$('#category_modal_add').modal('hide')	
		// ajax to load the category list again
		hidden_cat = $('#hidCat').val()
		$.post('/category_list', {hidden_cat:hidden_cat}, function(new_cat_data_list){
			$('.contentDiv').html(new_cat_data_list)
			$('#category_modal_list').modal('show')
		})
	})
})

// Editing the category
$(document).on('submit', '#catEditForm', function(event){
	event.preventDefault()
	$.post('/category_edit', $('#catEditForm').serialize(), function(){
		$('#category_modal_edit').modal('hide')	
		// ajax to load the category list again
		hidden_cat = $('#hiddenCat').val()
		$.post('/category_list', {hidden_cat:hidden_cat}, function(new_cat_data_list){
			$('.contentDiv').html(new_cat_data_list)
			$('#category_modal_list').modal('show')
		})
	})
})

$(document).on('click', '.cat_add_back_but', function(){
	$('#category_modal_add').modal('hide')
	hidCat = $('#hidCat').val()
	$.post('/category_list', {hidden_cat:hidCat}, function(new_cat_data_list){
		$('.contentDiv').html(new_cat_data_list)
		$('#category_modal_list').modal('show')	
	})
})

$(document).on('click', '.cat_edit_back_but', function(){
	$('#category_modal_edit').modal('hide')
	hidden_cat = $('#hiddenCat').val()
	$.post('/category_list', {hidden_cat:hidden_cat}, function(new_cat_data_list){
		$('.contentDiv').html(new_cat_data_list)
		$('#category_modal_list').modal('show')	
	})
})
