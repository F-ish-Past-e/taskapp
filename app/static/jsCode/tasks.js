// filtering for the task list
$('#filterStatus').change(function(){
	var clickedStatus = $(this).val();
	$.post('/tasksList', { clickedStatus: clickedStatus }, function(data) {
		$('#taskTbodyID').html(data);
	});
});

// this directs to a new url to edit current clicked task and show all its items
$(document).on('click', '#taskTbodyID tr', function(){
	clickedTaskRow = $(this).attr('id')
	window.location.href = `/divsPage/${clickedTaskRow}`;
})

// settings menu ckick
$(document).off("click", ".item_dropdown-button").on("click", ".item_dropdown-button", function(){
	var dropdownContent = $(this).next(".dropdown-content");
	dropdownContent.toggle('fast');
})

// trigger to display confirm html
$(document).on('click', '#deleteButton', function(){
	$.post('/taskDeleteConfirm', function(returnDelConfirm){
		$('.contentDiv').html(returnDelConfirm)
		$('#taskCheckDeleteModal').modal('show')
	})
})

// deleting task
$(document).off('click', '.taskDelConfirmBut').on('click', '.taskDelConfirmBut', function(){
	$.post('/taskDelete', {taskDeleteID:$('#hiddenTaskID').val()}, function(checkItems){
		if(checkItems=='outstanding_records'){
			$('.taskErrorHTML').show('fast')
			$('.taskErrorText').html('<span>Outstanding Item Records!</span>')
		}else{
			window.location.href = '/tasksList'
		}
	})
})

// back button from task edit
$(document).off('click', '.taskDelConfirmBack').on('click', '.taskDelConfirmBack', function(){
	$('#taskCheckDeleteModal').modal('hide')
})