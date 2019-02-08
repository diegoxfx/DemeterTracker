var thread;
var thread_draw;
var is_tracking;
var route_id;

function get_location() {
    var output = document.getElementById("out");

    if(!navigator.geolocation) {
	output.innerHTML = "<p>Geolocation is not supported by your browser</p>";
	return;
    }

    function success(position) {
	var latitude = position.coords.latitude;
	var longitude = position.coords.longitude;

	var current_date = new Date();

	function get_date() {
	    var now = new Date();
	    var y = now.getFullYear();
	    var m = now.getMonth() + 1;
	    var d = now.getDate();
	    return '' + y + '-' + (m < 10 ? '0' : '') + m + '-' +
		(d < 10 ? '0' : '') + d;
	}

	function get_time() {
	    var now = new Date();
	    var h = now.getHours();
	    var m = now.getMinutes();
	    var s = now.getSeconds();
	    return '' + (h < 10 ? '0' : '') + h + ':' + (m < 10? '0': '')
		+ m + ':' + (s < 10 ? '0' : '') + s;
	}

	var date = get_date();
	var time = get_time();

	var token = sessionStorage.getItem('token');

	var form = new FormData();
	form.append("route_id", route_id),
	form.append("latitude", latitude);
	form.append("longitude", longitude);
	form.append("hour", time);
	form.append("date", date);

	var post_url = document.location.origin + '/api/new_event';

	var settings = {
	    "async": true,
	    "crossDomain": true,
	    "url": post_url,
	    "method": "POST",
	    "headers": {
		"Authorization": token,
		"cache-control": "no-cache",
	    },
	    "processData": false,
	    "contentType": false,
	    "mimeType": "multipart/form-data",
	    "data": form
	}

	$.ajax(settings).done(function (response) {
	    console.log(response);
	});
    }

    function error() {
	output.innerHTML = "Unable to retrieve your location";
    }

    navigator.geolocation.getCurrentPosition(success, error);
}


function start_tracking() {
    get_location();
    draw_route_from_id(route_id);
    thread = setInterval(get_location, 1000*2);
    thread_draw = setInterval(function() {draw_route_from_id(route_id);}, 1000*10);
}

function stop_tracking() {
    clearInterval(thread);
    clearInterval(thread_draw);
}

function manage_track_event(button_id) {
    var text = document.getElementById(button_id).firstChild;
    if (is_tracking) {
	stop_tracking();
	is_tracking = false;
	text.data = "create and track";
    }
    else {
	create_route();
	start_tracking();
	is_tracking = true;
	text.data = "stop tracking";
    }    
}

function create_route() {
    var route_name = document.getElementById('id_route_set-0-name').value;
    
    var form = new FormData()
    form.append("name", route_name);

    var post_url = document.location.origin + '/api/new_route';
    var token = sessionStorage.getItem('token');
    
    var settings = {
	"async": false,
	"crossDomain": true,
	"url": post_url,
	"method": "POST",
	"headers": {
	    "Authorization": token,
	    "cache-control": "no-cache",
	},
	"processData": false,
	"contentType": false,
	"mimeType": "multipart/form-data",
	"data": form
    }

    $.ajax(settings).done(function (response) {
	data = JSON.parse(response);
	route_id = data.id
    });
}
