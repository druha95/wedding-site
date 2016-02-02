$(document).ready(function($) {

    if(window.location.hash != "") {
        window.setTimeout(function() {
            $(document).scrollTop($(document).scrollTop()-50);
        },  4);
    }

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

    $(window).scroll(function() {
        if ($(document).scrollTop() > 130) {
            $('nav').addClass('shrink');
            $('#getting-married').addClass('shrink');
        } else {
            $('nav').removeClass('shrink');
            $('#getting-married').removeClass('shrink');
        }
    });

    $(".form-horizontal select").on('change', function(event) {
        var value = $(this).val();
        if(value == "other" || value == "manila_other" || value == "boracay_other") {
            $("#" + $(event.target).closest("div")[0].id + "_other").css("display", "inline-block");
        } else {
            $("#" + $(event.target).closest("div")[0].id + "_other").css("display", "none");
        }
    });

    $(".navbar-element a").on("click", function() {
        window.setTimeout(function() {
            $(document).scrollTop($(document).scrollTop()-50);
        },  4);
    });

    //$("#smart-form-1, #smart-form-2").on("click", function(event) {
    //    event.preventDefault();
    //    return false;
    //})
});

