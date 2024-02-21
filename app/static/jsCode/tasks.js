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

$(document).off("click", ".item_dropdown-button").on("click", ".item_dropdown-button", function(){
	var dropdownContent = $(this).next(".dropdown-content");
	dropdownContent.toggle('fast');
})
