	$(function() {
			   
				/* @reload captcha
				------------------------------------------- */			   
				function reloadCaptcha(){
					$("#captcha").attr("src","php/captcha.php?r=" + Math.random());
				}
				
				$('.captcode').click(function(e){
					e.preventDefault();
					reloadCaptcha();
				});				
			   
				$( "#smart-form" ).validate({
				
						/* @validation states + elements 
						------------------------------------------- */
						errorClass: "error",
						validClass: "state-success",
						errorElement: "em",
						onkeyup: false,
						onclick: false,

						/* @validation rules 
						------------------------------------------ */
						rules: {
								name: {
										required: true,
										minlength: 3
								},		
								email: {
										required: false,
										email: true
								},
								number_of_guests: {
										required: true,
										minlength: 1
								},								
								// sendermessage: {
								// 		required: false,
								// 		minlength: 10
								// },
								// securitycode:{
								// 		required:true
								// }
						},
						
					
						messages:{
								name: {
										required: 'Who are you?',
										// minlength: 'Please enter a valid name.'
								},				
								email: {
										required: 'This field is required.',
										email: 'Please enter a valid email address.'
								},
								number_of_guests: {
										required: 'How many are coming?',
										minlength: 'How many are coming?'
								},														
								sendermessage: {
										required: 'Oops you forgot your message',
										minlength: 'Message must be at least 10 characters'
								},															
								securitycode:{
										required: 'Bitte gib den Code ein.'
								}
						},

						
						/* @ajax form submition 
						---------------------------------------------------- */						
						submitHandler:function(form) {
							$(form).ajaxSubmit({
								    target:'.result',			   
									beforeSubmit:function(){ 
											$('.form-footer').addClass('progress');
									},
									error:function(){
											$('.form-footer').removeClass('progress');
									},
									success:function(){
											$('.form-footer').removeClass('progress');
											$('.alert-success').show().delay(10000).fadeOut();
											$('#gogo').css({'display' : 'none'});
											$('.result').html('<h1 class="txtmagenta">Hooray! You have just RSVP\'d. We\'re so excited! :)</h1>');
											// if( $('.alert-error').length == 0){
											// 	$('#smart-form').resetForm();
												// reloadCaptcha();
											// }
									 }
							  });
						}
						// end submitHandler:
				});		
		
	});				
    