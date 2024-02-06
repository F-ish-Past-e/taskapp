clickedTaskRow = $('#hiddenTaskID').val()
contentLoad()
function contentLoad(){
	$.post('/taskEdit', {clickedTaskRow:clickedTaskRow}, function(taskeditreturn){
		$('.divs_content_one').html(taskeditreturn)
	})
	$.post('/item_list', {clickedTaskRow:clickedTaskRow}, function(tasklistreturn){
		$('.divs_content_two').html(tasklistreturn)
	})
}
