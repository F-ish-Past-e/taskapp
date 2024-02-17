// click event to show dialog priority list
$('.prioritiesClick').click(function(){
	hidden_pri_type = $('#hiddenPriType').val()
	$.post('/priority_list', {hidden_pri_type:hidden_pri_type}, function(task_pri_list_data){
		$('.contentDiv').html(task_pri_list_data)
		$('#pri_modal_list').modal('show')
	})
})

// displaying the task priority add html
$(document).off('click', '#pri_add_button').on('click', '#pri_add_button', function(){
	$('#pri_modal_list').modal('hide')
	hidPriType = $('#hidPriType').val()
	$.post('/priority_add', {hidPriType:hidPriType}, function(pri_add_return){
		$('.contentDiv').html(pri_add_return)
		$('#AddPriorityModal').modal('show')
	})
})

// custom js validation for the color and then the Priority submit as well
$(document).off('submit', '#priorityAddForm').on('submit', '#priorityAddForm', function(event){
	event.preventDefault()
	if(!$('#hiddenSelectedColor').val()){
		$('.errorHTML').show('fast')
		$('.errorText').html('<span>Please select a priority color!</span>')
	}else{
		$('.errorHTML').hide('fast')
		$.post('/priority_add', $('#priorityAddForm').serialize(), function(){
			$('#AddPriorityModal').modal('hide')
			hidden_pri_type = $('#hiddenPriType').val()
			$.post('/priority_list', {hidden_pri_type:hidden_pri_type}, function(task_pri_list_data){
				$('.contentDiv').html(task_pri_list_data)
				$('#pri_modal_list').modal('show')
			})
		})
	}
})

// To dispay the priority edit page
$(document).off('click', '#PriTbodyID tr').on('click', '#PriTbodyID tr', function(){
	clickedPriRow = $(this).attr('id')
	$('#pri_modal_list').modal('hide')
	$.post('/priority_edit', {clickedPriRow:clickedPriRow}, function(pri_edit_return){
		$('.contentDiv').html(pri_edit_return)
		$('#EditPriorityModal').modal('show')
		if($('#PriSelectedColor').val()=='Green'){
			$(".clickGreen, .clickOrange, .clickRed").removeClass("active");
			$('.clickGreen').addClass("active")
		}
		if($('#PriSelectedColor').val()=='Orange'){
			$(".clickGreen, .clickOrange, .clickRed").removeClass("active");
			$('.clickOrange').addClass("active")
		}
		if($('#PriSelectedColor').val()=='Red'){
			$(".clickGreen, .clickOrange, .clickRed").removeClass("active");
			$('.clickRed').addClass("active")
		}
	})
})

// to update the priorities
$(document).off('submit', '#priorityEditForm').on('submit', '#priorityEditForm', function(event){
	event.preventDefault()
	$('#EditPriorityModal').modal('hide')
	$.post('/priority_edit', $('#priorityEditForm').serialize(), function(){
		hidden_pri_type = $('#hiddenPriType').val()
		$.post('/priority_list', {hidden_pri_type:hidden_pri_type}, function(task_pri_list_data){
			$('.contentDiv').html(task_pri_list_data)
			$('#pri_modal_list').modal('show')
		})
	})
})

// back button when clicked on the priority add
$(document).off('click', '#priAddBack').on('click', '#priAddBack', function(){
	$('#AddPriorityModal').modal('hide')
	hidden_pri_type = $('#hiddenPriType').val()
	$.post('/priority_list', {hidden_pri_type:hidden_pri_type}, function(task_pri_list_data){
		$('.contentDiv').html(task_pri_list_data)
		$('#pri_modal_list').modal('show')
	})
})

// back button when clicked on the priority edit
$(document).off('click', '#priEditBack').on('click', '#priEditBack', function(){
	$('#EditPriorityModal').modal('hide')
	hidden_pri_type = $('#hiddenPriType').val()
	$.post('/priority_list', {hidden_pri_type:hidden_pri_type}, function(task_pri_list_data){
		$('.contentDiv').html(task_pri_list_data)
		$('#pri_modal_list').modal('show')
	})
})

// click to highlight the color selected
$(document).ready(function() {
	$(".clickGreen, .clickOrange, .clickRed").click(function() {
		$(".clickGreen, .clickOrange, .clickRed").removeClass("active");
		$(this).addClass("active");
		$('#PriSelectedColor').val($(this).val())
		$('#hiddenSelectedColor').val($(this).val())
	});
});
  