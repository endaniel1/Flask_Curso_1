$(document).ready(function(e){
	//Aqui ´para la peticion ajax del login
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

	//Aqui detenemos el submit del login
	$("#form-login").submit(function(e){
		e.preventDefault();
		ajax_login();
	});
});