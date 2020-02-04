$(document).ready(function(e){

	function ajax_login(){
		$.ajax({
			url:"/ajax-login",
			data:$("#form-login").serialize(),
			type:"POST",
			success:function(response){
				console.log(response);
			},error:function(errors){
				console.log(errors);
			}
		});	
	}



	$("#form-login").submit(function(e){
		e.preventDefault();
		ajax_login();
	});
});