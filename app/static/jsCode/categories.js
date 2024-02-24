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

// back button from the cat add page
$(document).on('click', '.cat_add_back_but', function(){
	$('#category_modal_add').modal('hide')
	hidCat = $('#hidCat').val()
	$.post('/category_list', {hidden_cat:hidCat}, function(new_cat_data_list){
		$('.contentDiv').html(new_cat_data_list)
		$('#category_modal_list').modal('show')	
	})
})

// back button from the cat edit page
$(document).on('click', '.cat_edit_back_but', function(){
	$('#category_modal_edit').modal('hide')
	hidden_cat = $('#hiddenCat').val()
	$.post('/category_list', {hidden_cat:hidden_cat}, function(new_cat_data_list){
		$('.contentDiv').html(new_cat_data_list)
		$('#category_modal_list').modal('show')	
	})
})

// trigger to display confirm html
$(document).off('click', '.cat_edit_del_but').on('click', '.cat_edit_del_but', function(){
	$('#category_modal_edit').modal('hide')
	$.post('/catDeleteConfirm', {catDeleteID:$('#clickedCatEditRow').val(), hiddenCat:$('#hiddenCat').val()}, function(returnDelConfirm){
		$('.contentDiv').html(returnDelConfirm)
		$('#catCheckDeleteModal').modal('show')
	})
})

// deleting category
$(document).off('click', '.catDelConfirmBut').on('click', '.catDelConfirmBut', function(){
	$.post('/catDelete', {catDeleteID:$('#clickedCatEditRow').val(), hiddenCat:$('#hiddenCat').val()}, function(checkTasks){
		if(checkTasks=='outstanding_records'){
			$('.catErrorHTML').show('fast')
			$('.catErrorText').html('<span>Records containing this category name!</span>')
		}else{
			$('#catCheckDeleteModal').modal('hide')
			hidden_cat = $('#hiddenCat').val()
			$.post('/category_list', {hidden_cat:hidden_cat}, function(new_cat_data_list){
				$('.contentDiv').html(new_cat_data_list)
				$('#category_modal_list').modal('show')	
			})
		}
	})
})

// back button from category delete
$(document).off('click', '.catDelConfirmBack').on('click', '.catDelConfirmBack', function(){
	$('#catCheckDeleteModal').modal('hide')
	$.post('/category_edit', {clickedCatEditRow:$('#clickedCatEditRow').val(), hiddenCat:$('#hiddenCat').val()}, function(new_cat_data_list){
		$('.contentDiv').html(new_cat_data_list)
		$('#category_modal_edit').modal('show')	
	})
})