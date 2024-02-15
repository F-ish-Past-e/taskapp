$('.prioritiesClick').click(function(){
	$.post('/priority_list', function(task_pri_list_data){
		$('.contentDiv').html(task_pri_list_data)
		$('#task_pri_list_modal_id').modal('show')
	})
})