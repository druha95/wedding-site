$(document).ready(function() { initialize(); });

function initialize(){
    var mapOptions = {
        center: new google.maps.LatLng(49.614376, 11.003710),
        zoom: 12,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    var map = new google.maps.Map(document.getElementById("map-wrap"), mapOptions);
                           
    var styles = [
					  {
					    stylers: [
					      { visibility: "simplified" },
					      { gamma: 1.56 },
					      { saturation: -10 },
					      { hue: "#f6efeb" }
					    ]
					  }
					];
	map.setOptions({styles: styles, scrollwheel: false});
	
	var info_window = new google.maps.InfoWindow({
        content: 'loading'
    });
    
    var herz = {
	  path: "M36.3,17.5L20,32.4L3.7,17.5c-4.2-4-4.2-10.3,0-14.2c3.8-3.4,9.9-3.4,13.7,0L20,5.6l2.6-2.3c3.7-3.4,9.8-3.4,13.6,0C40.5,7.2,40.5,13.5,36.3,17.5z",
	  fillColor: "#8b008b",
	  fillOpacity: 1,
	  scale: 1,
	  strokeColor: "white",
	  anchor: new google.maps.Point(20,30)
	};
    var entlas_keller = {
        url: 'static/img/pointer-entlas-keller.png',
        size: new google.maps.Size(80, 80),
        origin: new google.maps.Point(0,0),
    };
    var schloss_atzelsberg = {
        url: 'static/img/pointer-schloss-atzelsberg.png',
        size: new google.maps.Size(80, 80),
        origin: new google.maps.Point(0,0),
    };
    var nh_erlangen = {
        url: 'static/img/pointer-nh-erlangen.png',
        size: new google.maps.Size(80, 80),
        origin: new google.maps.Point(0,0),
    };

    var t = [];
    var x = [];
    var y = [];
    var h = [];
    var z = [];

    t.push('Frühschoppen');
    x.push(49.607865);
    y.push(11.003418);
    h.push('<p class="highlight-map txtmagenta">Frühschoppen<br>Aug 22, 1 pm</p><br><p class="map"><strong>Entlas Keller</strong><br>Cellar 5<br>91054 Erlangen</p><p class="map"><a href="https://www.google.com/maps/dir///@49.6080977,10.9294314,12z/data=!3m1!4b1!4m8!4m7!1m5!1m1!1s0x0:0x5913460112b87abc!2m2!1d11.00342!2d49.60801!1m0" target="_blank"><span class="entypo">&#59154;</span> Directions from here</a><br><a href="https://www.google.com/maps/dir///@49.6080977,10.9294314,12z/data=!3m1!4b1!4m8!4m7!1m0!1m5!1m1!1s0x0:0x5913460112b87abc!2m2!1d11.00342!2d49.60801" target="_blank"><span class="entypo">&#10150;</span> Directions to here</a><br><a href="static/files/Frühschoppen.ics"><span class="entypo">&#128197;</span> Add to iCal</a><br><a href="https://www.google.com/calendar/event?action=TEMPLATE&tmeid=Z3BwNTVodG9iaG1yY3I0ZXR2YTZldnJhb2sga2FyZW5qaWxsb25nQG0&tmsrc=karenjillong%40gmail.com"><span class="entypo">&#128197;</span> Add to Google calendar</a></p>');
    z.push(entlas_keller);

    t.push('Schloss Atzelsberg');
    x.push(49.626442);
    y.push(11.041818);
    h.push('<p class="highlight-map txtmagenta">Polterabend<br>Aug 21, 6 pm</p><br><p class="map"><strong>Schloss Atzelsberg</strong><br>Atzelsberg 1<br>91080 Marloffstein</p><p class="map"><a href="https://www.google.com/maps/dir/Schloss+Atzelsberg//@49.6268194,10.9678345,12z/data=!3m1!4b1!4m8!4m7!1m5!1m1!1s0x0:0x22915b22b5716d04!2m2!1d11.0418231!2d49.6267318!1m0" target="_blank"><span class="entypo">&#59154;</span> Directions from here</a><br><a href="https://www.google.com/maps/dir//Schloss+Atzelsberg/@49.6268194,10.9678345,12z/data=!3m1!4b1!4m8!4m7!1m0!1m5!1m1!1s0x0:0x22915b22b5716d04!2m2!1d11.0418231!2d49.6267318" target="_blank"><span class="entypo">&#10150;</span> Directions to here</a><br><a href="static/files/Polterabend von Karen und Michael.ics"><span class="entypo">&#128197;</span> Add to iCal</a><br><a href="https://www.google.com/calendar/event?action=TEMPLATE&tmeid=dTFmcjh1NzJkODFobTJicTgya24wc2h2ZTAga2FyZW5qaWxsb25nQG0&tmsrc=karenjillong%40gmail.com"> <span class="entypo">&#128197;</span> Add to Google calendar</a></p>');
    z.push(schloss_atzelsberg);    

    t.push('NH Erlangen');
    x.push(49.592126);
    y.push(11.007143);
    h.push('<p class="highlight-map txtmagenta">Hotel check-in<br>Aug 21</p><br><p class="map"><strong>NH Erlangen</strong><br>Beethovenstraße 3<br>91052 Erlangen</p><p class="map"><a href="https://www.google.com/maps/dir///@49.5893208,11.0068925,17z/data=!4m8!4m7!1m5!1m1!1s0x0:0x3058c3523d492b13!2m2!1d11.0074023!2d49.5901763!1m0" target="_blank"><span class="entypo">&#59154;</span> Directions from here</a><br><a href="https://www.google.com/maps/dir///@49.590264,10.9334137,12z/data=!3m1!4b1!4m8!4m7!1m0!1m5!1m1!1s0x0:0x3058c3523d492b13!2m2!1d11.0074023!2d49.5901763" target="_blank"><span class="entypo">&#10150;</span> Directions to here</a><br><a href="static/files/Check into Hotel NH Erlangen.ics"><span class="entypo">&#128197;</span> Add to iCal</a><br><a href="https://www.google.com/calendar/event?action=TEMPLATE&tmeid=cjZlbW5yZjVkZ3RhcmgxNmd2dmZnMWFnc2sga2FyZW5qaWxsb25nQG0&tmsrc=karenjillong%40gmail.com"><span class="entypo">&#128197;</span> Add to Google calendar</a></p>');
    z.push(nh_erlangen);

    var i = 0;
    for ( item in t ) {
        var m = new google.maps.Marker({
            map:       map,
            animation: google.maps.Animation.DROP,
            title:     t[i],
            position:  new google.maps.LatLng(x[i],y[i]),
            html:      h[i],
            icon: 	   z[i]
        });

        google.maps.event.addListener(m, 'click', function() {
            info_window.setContent(this.html);
            info_window.open(map, this);
        });
        i++;
    }		
}

google.maps.event.addDomListener(window, 'load', initialize);

