function login_js() {
    var username = document.getElementById('id_username').value;
    var password = document.getElementById('id_password').value;

    var post_url = document.location.origin + '/api/login';

    var form = new FormData();
    form.append("username", username);
    form.append("password", password);

    var settings = {
	"async": false,
	"crossDomain": true,
	"url": post_url,
	"method": "POST",
	"headers": {
	    "cache-control": "no-cache",
	    "Postman-Token": "8fd8c326-41f7-4315-b583-810298f1828f"
	},
	"processData": false,
	"contentType": false,
	"mimeType": "multipart/form-data",
	"data": form
    }

    var token;

    $.ajax(settings).done(function (response) {
	data = JSON.parse(response);
	token = "Token " + data.token;
    });
    sessionStorage.setItem('token', token);
}
