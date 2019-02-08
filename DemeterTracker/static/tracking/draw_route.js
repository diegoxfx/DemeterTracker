function draw_route_from_id(route_id) {
    var coords;

    var form = new FormData()
    form.append("id", route_id);
    
    var post_url = document.location.origin + '/api/get_events';
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
	coords = data;
    });
    

    var map = new google.maps.Map(document.getElementById('map'), {
	zoom: 15,
	center: coords[0],
	mapTypeId: 'terrain'
    });

    
    var route_path = new google.maps.Polyline({
	path: coords,
	geodesic: true,
	strokeColor: '#FF0000',
	strokeOpacity: 1.0,
	strokeWeight: 2
    });
    
    route_path.setMap(map);
}

function draw_route() {
    var map, infoWindow;

    var route_id = document.getElementById('id_routes').value;
    draw_route_from_id(route_id);
}
