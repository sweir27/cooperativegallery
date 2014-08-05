$(document).ready(function() {
	display_main_artists();
	display_first_artist();
});

function display_main_artists() {
	for (a in am_first) {
		var name = am_first[a].name;
		var biography = am_first[a].biography;

		var artist_el = "<li class='artist_name'><div class='artist_link'>"+name+"</div></li>";
		$("#artists_list").append(artist_el);
	}
}

function display_first_artist() {
	var first_name = am_first[0].name;
	var first_bio = am_first[0].biography;
	$("#artist_title").html(first_name);
	$("#artist_statement").html(first_bio);
}

$("body").on('click', '.artist_name', function(e) {
	var artist_name = $('> .artist_link', this).text();
	$("#artist_title").html('');
	$("#artist_title").html(artist_name);
	$("#artist_statement").html('');
	$("#images").html('');
	$.ajax({
        url: "/ajax_get_artist_image/",
        type: "POST",
        data: { 
        	name: artist_name,
        	csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value 
        },
        success: function(data) {
        	var artist = JSON.parse(data["artist"])
        	$("#artist_statement").html(artist[0].biography);

        	var artwork = JSON.parse(data["artwork"])
        	if (artwork.length > 0) {
        		for (var a in artwork) {
        			if (typeof artwork[a].image != 'object') {
        				var url = '/media/'+artwork[a].image
        				$("#images").append("<img class='test_img' src='"+url+"'></img>")
        			}
        		}
        	}
        },
        error: function (jqXHR, textStatus, errorThrown) {
	        // console.log(jqXHR.responseText);
	        // console.log(errorThrown)
	    }
    });
});