$(function(){

	let validator_flag = [false,false,false];
	console.log("*****"); 
	function get_form_fields(){
		let $username = $('#id_username');
		let $pass1 = $('#id_password1');
		let $pass2 = $('#id_password2');
		let $email = $('#id_email');

		return {
				username: $username,
				email: $email,
				password1: $pass1,
				password2:$pass2
			   }
	}
	const form_fields = get_form_fields();

	function set_errors($where, error_text){
		$where.after('<h4 style="color:#cc0000; display:none">'+error_text+'</h4>')
		
	}
	function set_username_error_text(){
		let form_fields = get_form_fields()
		set_errors(form_fields.username, "Username Already In Use");

	}
	function set_email_error_text(){
		let form_fields = get_form_fields()
		set_errors(form_fields.email, "Email Id Already Exist");
	}

	function set_password_error_text(){
		let form_fields = get_form_fields()
		set_errors(form_fields.password2, "Password Does Not Match");
	}

	function show_errors($where){
		$where.next().css('display','block');
	}

	function hide_errors($where){
		$where.next().css('display','none');
	}

	set_username_error_text();
	set_email_error_text();
	set_password_error_text();

	function set_validators(){
		form_fields.username.on('focusout', ()=>{
			let value = form_fields.username.val();
			let user_flag = false
			$.ajax({
				type: "GET",
				url : "http://127.0.0.1:8000/user?user="+value,
				success: (data)=>{
					console.log(data.result)
					if (data.result === true){
						console.log(user_flag)
						user_flag = true
						console.log(user_flag)
						if (user_flag === true){
						$('#id_username').css({'border' : '1px solid #cc0000'});
						show_errors(form_fields.username)
						validator_flag[0] = false;
						if (validator_flag[0] == true && validator_flag[1] == true && validator_flag[2] == true){
							console.log("teeno true hai")
							$('#register_button').removeAttr('disabled')
						}

						else{
							console.log("teeno tru nahi hai");
							$('#register_button').attr('disabled',true);
						}
						}
					}
					else{

						if (validator_flag[0] == true && validator_flag[1] == true && validator_flag[2] == true){
							console.log("teeno true hai")
							$('#register_button').removeAttr('disabled')
						}

						else{
							console.log("teeno tru nahi hai");
							$('#register_button').attr('disabled',true);
						}
						validator_flag[0] = true;
					}
				}
			});
		});

		form_fields.email.on('focusout', ()=>{
			let value = form_fields.email.val();
			console.log(value)
			let email_flag = false
			$.ajax({
				type: "GET",
				url : "http://127.0.0.1:8000/email?email="+value,
				success: (data)=>{
					console.log("email "+data.result)
					if (data.result === true){
						console.log("email "+email_flag)
						email_flag = true
						console.log("email "+email_flag)
						if (email_flag === true){
							$('#id_email').css({'border' : '1px solid #cc0000'});
							show_errors(form_fields.email);
							validator_flag[1] = false;
							if (validator_flag[0] == true && validator_flag[1] == true && validator_flag[2] == true){
							console.log("teeno true hai")
							$('#register_button').removeAttr('disabled')
						}

						else{
							console.log("teeno tru nahi hai");
							$('#register_button').attr('disabled',true);
						}
						}
						
					}
					else{
						validator_flag[1] = true;

						if (validator_flag[0] == true && validator_flag[1] == true && validator_flag[2] == true){
							console.log("teeno true hai")
							$('#register_button').removeAttr('disabled')
						}

						else{
							console.log("teeno tru nahi hai");
							$('#register_button').attr('disabled',true);
						}

					}
				}
			});
		});

		form_fields.password2.on('keyup', ()=>{
			if (form_fields.password1.val() === form_fields.password2.val()){
				$('#id_password2').css({'border' : 0});
				$('#id_password1').css({'border' : 0});
				hide_errors(form_fields.password2)
				validator_flag[2] = true;

				if (validator_flag[0] == true && validator_flag[1] == true && validator_flag[2] == true){
					console.log("teeno true hai")
					$('#register_button').removeAttr('disabled')
				}

				else{
					console.log("teeno tru nahi hai");
				}


			}
			else{
				$('#id_password2').css({'border' : '1px solid #cc0000'});
				$('#id_password1').css({'border' : '1px solid #cc0000'});
				show_errors(form_fields.password2);
				validator_flag[2] = false;
			}

		});

		form_fields.password1.on('focusout', ()=>{
			if (form_fields.password1.val() === form_fields.password2.val()){
				$('#id_password2').css({'border' : 0});
				$('#id_password1').css({'border' : 0});
				hide_errors(form_fields.password2)
				validator_flag[2] = true;
			}
			else{
				$('#id_password2').css({'border' : '1px solid #cc0000'});
				$('#id_password1').css({'border' : '1px solid #cc0000'});
				show_errors(form_fields.password2);
				validator_flag[2] = false;
			}
		});

		form_fields.email.on('focus', ()=>{
			$('#id_email').css({'border' : 0});
			validator_flag[1] = true;
			hide_errors(form_fields.email)
		});
		form_fields.password2.on('focus', ()=>{
			$('#id_password2').css({'border' : 0});
			$('#id_password1').css({'border' : 0});
			validator_flag[2] = true
			hide_errors(form_fields.password2)
		});
		form_fields.username.on('focus', ()=>{
			$('#id_username').css({'border' : 0});
			validator_flag[0] = true;
			hide_errors(form_fields.username)
		});

		
	}
	set_validators();
	$('#register_button').attr('disabled',true);
	$('button[type="submit"]:disabled').css('background-color','black');
	$('button[type="submit"]').css('background-color','white');
});
