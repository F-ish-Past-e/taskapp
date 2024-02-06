$('#add_item_but').click(function(){
	hidden_task_id = $('#hiddenTaskID').val()
	$.post('/item_add', {hidden_task_id:hidden_task_id}, function(itemaddreturn){
		$('.itemAddContentDiv').html(itemaddreturn)
	})
})

$(document).off('submit', '#itemAddForm').on('submit', '#itemAddForm', function(event){
	event.preventDefault()
	$.post('/item_add', $('#itemAddForm').serialize(), function(){
		$('#AddItemModal').modal('hide')
		window.location.reload()
	})
})

$(document).on('click', '#myTbodyID tr', function(){
	clickItemRow = $(this).attr('id')
	$.post('/item_edit', {clickItemRow:clickItemRow}, function(itemEditReturn){
		$('.itemEditContentDiv').html(itemEditReturn)
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