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
			   
    $( "#smart-form-1" ).validate({

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
                    }
            },


            messages:{
                    name: {
                            required: 'Oops! You forgot to enter your full name.'
                            // minlength: 'Please enter a valid name.'
                    }
            },

						
						/* @ajax form submition 
						---------------------------------------------------- */						
            submitHandler:function(form) {
                $(form).ajaxSubmit({
                        target:'.result',
                        beforeSubmit:function(){
                            $(".click_checkbox").css("display", "none");
                            var flag = false;
                            for(var i=0; i<$("input:radio[name=yes_no]").length; i++) {
                                if($($("input:radio[name=yes_no]")[i])[0].checked) {
                                    flag = true;
                                }
                            }
                            if(!flag) {
                                $(".click_checkbox").css("display", "inline-block");
                                return false;
                            };
                            $('#loading_gif-1').css({'display' : 'block'});
                            $('#gogo-1').css({'display' : 'none'});
                        },
                        error:function(){
                                $('.form-footer').removeClass('progress');
                        },
                        success:function(){
                                $('#loading_gif-1').css({'display' : 'none'});
                                $('.alert-success').show().delay(10000).fadeOut();
                                $('.result').html('<h1 class="txtmagenta">Sad that we can’t celebrate with you…</h1>');
                                // if( $('.alert-error').length == 0){
                                // 	$('#smart-form').resetForm();
                                    // reloadCaptcha();
                                // }
                         }
                  });
            }
            // end submitHandler:
    });

                $( "#smart-form-2" ).validate({

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
								}
						},


						messages:{
								name: {
										required: 'Oops! You forgot to enter your full name.'
										// minlength: 'Please enter a valid name.'
								}
						},


						/* @ajax form submition
						---------------------------------------------------- */
						submitHandler:function(form) {
							$(form).ajaxSubmit({
								    target:'.result',
									beforeSubmit:function(){
                                        $(".click_checkbox").css("display", "none");
                                        var flag = false;
                                        for(var i=0; i<$("input:radio[name=yes_no]").length; i++) {
                                            if($($("input:radio[name=yes_no]")[i])[0].checked) {
                                                flag = true;
                                            }
                                        }
                                        if(!flag) {
                                            $(".click_checkbox").css("display", "inline-block");
                                            return false;
                                        };
                                        $('#loading_gif-2').css({'display' : 'block'});
                                        $('#gogo-2').css({'display' : 'none'});
									},
									error:function(){
											$('.form-footer').removeClass('progress');
									},
									success:function(){
                                            $('#loading_gif-2').css({'display' : 'none'});
											$('.alert-success').show().delay(10000).fadeOut();
											$('.result').html('<h1 class="txtmagenta">Woohoo! Can\'t wait to celebrate with you!</h1>');
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
    