$(document).ready(function(){
    //Click events
    $('.toTop').click(function(){
        $('html, body').animate({scrollTop : 0},1800);
        return false;
    });
    $('.link1').click(function(){
        $('html, body').animate({scrollTop: $('#the-party').offset().top-50}, 1000);
        return false;
    });
    $('.link2').click(function(){
        $('html, body').animate({scrollTop: $('#night-after').offset().top-50}, 1000);
        return false;
    });
    $('.link3').click(function(){
        $('html, body').animate({scrollTop: $('#day-after').offset().top-50}, 1000);
        return false;
    });
    $('.link4').click(function(){
        $("html, body").animate({scrollTop: $('#rsvp').offset().top-35}, 1000);
        return false;
    });
    $('.link5').click(function(){
        $('html, body').animate({scrollTop: $('#instagram').offset().top-50}, 1000);
        return false;
    });
    $('.link6').click(function(){
        $('html, body').animate({scrollTop: $('#the-party').offset().top}, 1000);
        $('#nav-mobile').removeClass('open');
        return false;
    });
    $('.link7').click(function(){
        $('html, body').animate({scrollTop: $('#night-after').offset().top}, 1000);
        $('#nav-mobile').removeClass('open');
        return false;
    });
    $('.link8').click(function(){
        $("html, body").animate({scrollTop: $('#day-after').offset().top}, 1000);
        $('#nav-mobile').removeClass('open');
        return false;
    });
    $('.link9').click(function(){
        $("html, body").animate({scrollTop: $('#rsvp').offset().top}, 1000);
        $('#nav-mobile').removeClass('open');
        return false;
    });
    $('.link10').click(function(){
        $("html, body").animate({scrollTop: $('#instagram').offset().top}, 1000);
        $('#nav-mobile').removeClass('open');
        return false;
    });
});