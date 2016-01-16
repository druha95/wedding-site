$(document).ready(function($) {
    $("input:radio[name=yes_no]").click(function() {
        var value = $(this).val();
        if(value == 'rsvp') {
            $("#rsvp-form-mini").css('display', 'none');
            $("#rsvp-form").css('display', 'block');
            $("#guest-form").css('display', 'block');
        } else if(value == 'rsvp_mini') {
            $("#rsvp-form-mini").css('display', 'block');
            $("#rsvp-form").css('display', 'none');
            $("#guest-form").css('display', 'none');
        }
    });
});

$(document).ready(function($) {
    $("#id_number_of_guests").on('change', function() {
        for(var i=1; i<=5; i++) {
            $(".guest_form_" + i).css('display', "none");
        }

        var value = $(this).val();

        for(var j=1; j<=value; j++) {
            $(".guest_form_" + j).css('display', "block");
        }
    });
});