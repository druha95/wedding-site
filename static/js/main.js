$(document).ready(function($) {
	// build tween
	var tween = TweenMax.fromTo("#logohome", 1, 
				{marginTop: -300, ease: Back.easeOut},
				{marginTop: -18, ease: Back.easeOut, delay: 4}
				);

	// build scene
	var scene = new ScrollScene({triggerElement: "section#home", triggerHook: 0.6})
					.setTween(tween)
					.addTo(controller);
});
$(document).ready(function($) {
	// build tween
	var tween = TweenMax.fromTo("#welcome", 0.5, 
				{marginTop: -400, ease: Back.easeOut},
				{marginTop: 60, ease: Back.easeOut}
				);

	// build scene
	var scene = new ScrollScene({triggerElement: "section#getting-married", triggerHook: 0.6})
					.setTween(tween)
					.addTo(controller);
});
$(document).ready(function($) {
	// build tween
	var tween = TweenMax.fromTo("#bubble-finally", 0.2,
				{scale: 0, ease: Back.easeOut},
				{scale: 1, ease: Back.easeOut, delay: 1.8}
				);

	// build scene
	var scene = new ScrollScene({triggerElement: "section#getting-married", triggerHook: 0.4})
					.setTween(tween)
					.addTo(controller);
});
$(document).ready(function($) {
	// build tween
	var tween = TweenMax.fromTo("#bubble-yes", 0.5,
				{scale: 0, ease: Back.easeOut},
				{scale: 1, ease: Back.easeOut, delay: 0.8}
				);

	// build scene
	var scene = new ScrollScene({triggerElement: "section#getting-married", triggerHook: 0.4})
					.setTween(tween)
					.addTo(controller);
});
//$(document).ready(function($) {
//	// build tween
//	var tween = TweenMax.fromTo("img#bubble-the-polterweekend", 0.5,
//				{marginTop: -250, ease: Back.easeOut, rotation: 0},
//				{marginTop: 50, ease: Back.easeOut, rotation: 350}
//				);
//
//	// build scene
//	var scene = new ScrollScene({triggerElement: "section#the-polterweekend", triggerHook: 0.4})
//					.setTween(tween)
//					.addTo(controller);
//});
$(document).ready(function($) {
	// build tween
	var tween = TweenMax.fromTo("img#karen", 0.5,
				{marginLeft: -2000, rotation: -360, ease: Back.easeOut},
				{marginLeft: 0, rotation: 0, ease: Back.easeOut, delay: 0.5}
				);

	// build scene
	var scene = new ScrollScene({triggerElement: "section#couple", triggerHook: 0.4})
					.setTween(tween)
					.addTo(controller);
});
$(document).ready(function($) {
	// build tween
	var tween = TweenMax.fromTo("#karentxt", 0.5,
				{opacity: 0},
				{opacity: 1, delay: 0.5}
				);

	// build scene
	var scene = new ScrollScene({triggerElement: "section#couple", triggerHook: 0.4})
					.setTween(tween)
					.addTo(controller);
});
$(document).ready(function($) {
	// build tween
	var tween = TweenMax.fromTo("img#michael", 0.5, 
				{marginLeft: 2000, rotation: 0, ease: Back.easeOut},
				{marginLeft: 0, rotation: -360, ease: Back.easeOut, delay: 1.2}
				);

	// build scene
	var scene = new ScrollScene({triggerElement: "section#couple", triggerHook: 0.4})
					.setTween(tween)
					.addTo(controller);
});
$(document).ready(function($) {
	// build tween
	var tween = TweenMax.fromTo("#jotxt", 0.5, 
				{opacity: 0},
				{opacity: 1, delay: 1.2}
				);

	// build scene
	var scene = new ScrollScene({triggerElement: "section#couple", triggerHook: 0.4})
					.setTween(tween)
					.addTo(controller);
});
$(document).ready(function($) {
	// build tween
	var tween = TweenMax.fromTo("#bubble-the-couple", 0.5,
                    {marginTop: -250, ease: Back.easeOut, rotation: 0},
                    {marginTop: 50, ease: Back.easeOut, rotation: 350}
				);

	// build scene
	var scene = new ScrollScene({triggerElement: "section#couple", triggerHook: 0.6})
					.setTween(tween)
					.addTo(controller);
});
// $(document).ready(function($) {
// 	// build tween
// 	var tween = TweenMax.fromTo("img#bubble-die-trauzeugen", 0.5, 
// 				{scale: 0, ease: Back.easeOut, rotation: 0},
// 				{scale: 1, ease: Back.easeOut, rotation: 360}
// 				);

// 	// build scene
// 	var scene = new ScrollScene({triggerElement: "section#die-trauzeugen", triggerHook: 0.5})
// 					.setTween(tween)
// 					.addTo(controller);
// });
// $(document).ready(function($) {
// 	// build tween
// 	var tween = TweenMax.fromTo("img#henni", 0.5, 
// 				{scale: 0, rotation: -100, ease: Back.easeOut},
// 				{scale: 1, rotation: 0, ease: Back.easeOut, delay: 0.5}
// 				);

// 	// build scene
// 	var scene = new ScrollScene({triggerElement: "section#die-trauzeugen", triggerHook: 0.5})
// 					.setTween(tween)
// 					.addTo(controller);
// });
// $(document).ready(function($) {
// 	// build tween
// 	var tween = TweenMax.fromTo("#hennitxt", 0.5, 
// 				{opacity: 0},
// 				{opacity: 1, delay: 0.5}
// 				);

// 	// build scene
// 	var scene = new ScrollScene({triggerElement: "section#die-trauzeugen", triggerHook: 0.5})
// 					.setTween(tween)
// 					.addTo(controller);
// });
// $(document).ready(function($) {
// 	// build tween
// 	var tween = TweenMax.fromTo("img#julian", 0.5, 
// 				{scale: 0, rotation: 100, ease: Back.easeOut},
// 				{scale: 1, rotation: 0, ease: Back.easeOut, delay: 1.2}
// 				);

// 	// build scene
// 	var scene = new ScrollScene({triggerElement: "section#die-trauzeugen", triggerHook: 0.5})
// 					.setTween(tween)
// 					.addTo(controller);
// });
// $(document).ready(function($) {
// 	// build tween
// 	var tween = TweenMax.fromTo("#juliantxt", 0.5, 
// 				{opacity: 0},
// 				{opacity: 1, delay: 1.2}
// 				);

// 	// build scene
// 	var scene = new ScrollScene({triggerElement: "section#die-trauzeugen", triggerHook: 0.5})
// 					.setTween(tween)
// 					.addTo(controller);
// });
// $(document).ready(function($) {
// 	// build tween
// 	var tween = TweenMax.fromTo("img#steffi", 0.5, 
// 				{scale: 0, rotation: -100, ease: Back.easeOut},
// 				{scale: 1, rotation: 0, ease: Back.easeOut, delay: 1.9}
// 				);

// 	// build scene
// 	var scene = new ScrollScene({triggerElement: "section#die-trauzeugen", triggerHook: 0.5})
// 					.setTween(tween)
// 					.addTo(controller);
// });
// $(document).ready(function($) {
// 	// build tween
// 	var tween = TweenMax.fromTo("#steffitxt", 0.5, 
// 				{opacity: 0},
// 				{opacity: 1, delay: 0.5}
// 				);

// 	// build scene
// 	var scene = new ScrollScene({triggerElement: "section#die-trauzeugen", triggerHook: 0.5})
// 					.setTween(tween)
// 					.addTo(controller);
// });
$(document).ready(function($) {
	// build tween
	var tween = TweenMax.fromTo("img#bubble-facts", 0.5,
				{marginTop: -120, ease: Back.easeOut},
				{marginTop: 50, ease: Back.easeOut}
				);

	// build scene
	var scene = new ScrollScene({triggerElement: "section#story", triggerHook: 0.7})
					.setTween(tween)
					.addTo(controller);
});
$(document).ready(function($) {
	// build tween
	var tween = TweenMax.fromTo("div#date1", 0.5,
				{marginLeft: "-200%", width: "100%"},
				{marginLeft: 0}
				);

	// build scene
	var scene = new ScrollScene({triggerElement: "section#story", triggerHook: 0.5})
					.setTween(tween)
					.addTo(controller);
});

$(document).ready(function($) {
    // build tween
    var tween = TweenMax.fromTo("img#hbs", 0.5,
        {marginLeft: "-200%"},
        {marginLeft: 0}
    );

    // build scene
    var scene = new ScrollScene({triggerElement: "section#story", triggerHook: 0.5})
        .setTween(tween)
        .addTo(controller);
});
// $(document).ready(function($) {
// 	// build tween
// 	var tween = TweenMax.fromTo("div#duesseldorf", 0.3, 
// 				{scale: 0, ease: Back.easeOut},
// 				{scale: 1, ease: Back.easeOut, delay: 0.5}
// 				);

// 	// build scene
// 	var scene = new ScrollScene({triggerElement: "section#zusammensein", triggerHook: 0.5})
// 					.setTween(tween)
// 					.addTo(controller);
// });
$(document).ready(function($) {
	// build tween
	var tween = TweenMax.fromTo("div#date2", 0.5,
				{marginLeft: "300%", width: "100%"},
				{marginLeft: 0, delay: 1}
				);

	// build scene
	var scene = new ScrollScene({triggerElement: "section#story", triggerHook: 0.5})
					.setTween(tween)
					.addTo(controller);
});

$(document).ready(function($) {
    // build tween
    var tween = TweenMax.fromTo("img#champagne", 0.5,
        {marginLeft: "300%"},
        {marginLeft: 0, delay: 1}
    );

    // build scene
    var scene = new ScrollScene({triggerElement: "section#story", triggerHook: 0.5})
        .setTween(tween)
        .addTo(controller);
});


// $(document).ready(function($) {
// 	// build tween
// 	var tween = TweenMax.fromTo("div#malediven", 0.3, 
// 				{scale: 0, ease: Back.easeOut},
// 				{scale: 1, ease: Back.easeOut, delay: 1.5}
// 				);

// 	// build scene
// 	var scene = new ScrollScene({triggerElement: "section#zusammensein", triggerHook: 0.5})
// 					.setTween(tween)
// 					.addTo(controller);
// });
// $(document).ready(function($) {
// 	// build tween
// 	var tween = TweenMax.fromTo("div#warum-nicht", 0.5, 
// 				{scale: 0.5, opacity: 0},
// 				{scale: 1.2, opacity: 1, delay: 2}
// 				);

// 	// build scene
// 	var scene = new ScrollScene({triggerElement: "section#zusammensein", triggerHook: 0.3})
// 					.setTween(tween)
// 					.addTo(controller);
// });
$(document).ready(function($) {
	// build tween
	var tween = TweenMax.fromTo("img#globe-lights", 0.5, 
				{marginTop: "-40%", ease: Back.easeOut},
				{marginTop: "-10%", ease: Back.easeOut, delay: 2.6}
				);

	// build scene
	var scene = new ScrollScene({triggerElement: "section#the-party", triggerHook: 0.5})
					.setTween(tween)
					.addTo(controller);
});
$(document).ready(function($) {
	// build tween
	var tween = TweenMax.fromTo("img#bubble-das-fest", 0.5,
				{marginTop: -150, ease: Back.easeOut},
				{marginTop: "2%", ease: Back.easeOut }
				);

	// build scene
	var scene = new ScrollScene({triggerElement: "section#the-party", triggerHook: 0.6})
					.setTween(tween)
					.addTo(controller);
});
$(document).ready(function($) {
	// build tween
	var tween = TweenMax.fromTo("img#location-arrow", 0.3, 
				{scale: 0, ease: Back.easeOut, marginTop: 300},
				{scale: 1, ease: Back.easeOut, marginTop:0, delay: 1.5 }
				);

	// build scene
	var scene = new ScrollScene({triggerElement: "section#the-party", triggerHook: 0.6})
					.setTween(tween)
					.addTo(controller);
});
$(document).ready(function($) {
	// build tween
	var tween = TweenMax.fromTo("img#location-arrow-2", 0.3, 
				{scale: 0, ease: Back.easeOut, marginTop: -300, marginRight: -300},
				{scale: 1, ease: Back.easeOut, marginTop: 0,  marginRight: 0, delay: 1.8 }
				);

	// build scene
	var scene = new ScrollScene({triggerElement: "section#the-party", triggerHook: 0.6})
					.setTween(tween)
					.addTo(controller);
});
$(document).ready(function($) {
	// build tween
	var tween = TweenMax.fromTo("img#location-arrow-3", 0.3, 
				{scale: 0, ease: Back.easeOut, marginTop: -300, marginRight: 300},
				{scale: 1, ease: Back.easeOut, marginTop: 0,  marginRight: 0, delay: 2.1 }
				);

	// build scene
	var scene = new ScrollScene({triggerElement: "section#the-party", triggerHook: 0.6})
					.setTween(tween)
					.addTo(controller);
});
$(document).ready(function($) {
	// build tween
	var tween = TweenMax.fromTo("img#party1", 0.3, 
				{scale: 0, ease: Back.easeOut, rotation:0},
				{scale: 1, ease: Back.easeOut, rotation:80, delay: 3 }
				);

	// build scene
	var scene = new ScrollScene({triggerElement: "section#the-party", triggerHook: 0.6})
					.setTween(tween)
					.addTo(controller);
});
$(document).ready(function($) {
	// build tween
	var tween = TweenMax.fromTo("img#party2", 0.3, 
				{scale: 0, ease: Back.easeOut, rotation:0},
				{scale: 1, ease: Back.easeOut, rotation:360, delay: 3.3 }
				);

	// build scene
	var scene = new ScrollScene({triggerElement: "section#the-party", triggerHook: 0.6})
					.setTween(tween)
					.addTo(controller);
});
$(document).ready(function($) {
	// build tween
	var tween = TweenMax.fromTo("img#bubble-night-after", 0.5, 
				{marginTop: -250, ease: Back.easeOut},
				{marginTop: "3%", ease: Back.easeOut }
				);

	// build scene
	var scene = new ScrollScene({triggerElement: "section#night-after", triggerHook: 0.6})
					.setTween(tween)
					.addTo(controller);
});
$(document).ready(function($) {
	// build tween
	var tween = TweenMax.fromTo("img#bubble-day-after", 0.5, 
				{marginTop: -250, ease: Back.easeOut},
				{marginTop: "3%", ease: Back.easeOut }
				);

	// build scene
	var scene = new ScrollScene({triggerElement: "section#day-after", triggerHook: 0.6})
					.setTween(tween)
					.addTo(controller);
});
$(document).ready(function($) {
	// build tween
	var tween = TweenMax.fromTo("img#hands", 0.5,
				{marginTop: -700, ease: Bounce},
				{marginTop: 0, ease: Bounce, delay: 0.5}
				);

	// build scene
	var scene = new ScrollScene({triggerElement: "section#wedding", triggerHook: 0.6})
					.setTween(tween)
					.addTo(controller);
});
$(document).ready(function($) {
	// build tween
	var tween = TweenMax.fromTo("img#bubble-trauung", 0.5, 
				{marginTop: -250, ease: Back.easeOut},
				{marginTop: "1.5%", ease: Back.easeOut }
				);

	// build scene
	var scene = new ScrollScene({triggerElement: "section#the-party", triggerHook: 0.6})
					.setTween(tween)
					.addTo(controller);
});
$(document).ready(function($) {
	// build tween
	var tween = TweenMax.fromTo("img#bubble-i-will-2", 0.5, 
				{marginTop: -250, ease: Back.easeOut},
				{marginTop: 40, ease: Back.easeOut }
				);

	// build scene
	var scene = new ScrollScene({triggerElement: "section#rsvp", triggerHook: 0.6})
					.setTween(tween)
					.addTo(controller);
});
$(document).ready(function($) {
	// build tween
	var tween = TweenMax.fromTo("img#bubble-to-the-party", 0.5, 
				{scale: 0, ease: Back.easeOut, rotation: 0},
				{scale: 1, ease: Back.easeOut, rotation: 365, delay: 1}
				);

	// build scene
	var scene = new ScrollScene({triggerElement: "section#rsvp", triggerHook: 0.6})
					.setTween(tween)
					.addTo(controller);
});
$(document).ready(function($) {
	// build tween
	var tween = TweenMax.fromTo("img#bubble-googlemap", 0.5, 
				{marginBottom: -200, ease: Back.easeOut},
				{marginBottom: 10, ease: Back.easeOut}
				);

	// build scene
	var scene = new ScrollScene({triggerElement: "section#googlemap", triggerHook: 0.4})
					.setTween(tween)
					.addTo(controller);
});