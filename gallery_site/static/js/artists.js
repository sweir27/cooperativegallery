$(document).ready(function() {
	display_main_artists();
});

function display_main_artists() {
	for (a in am_first) {
		var name = am_first[a].name;
		var biography = am_first[a].biography;

		var artist_el = "<li class='artist_name'>"+name+"</li>";
		$("#artists_list").append(artist_el);
	}

	var first_name = am_first[0].name;
	var first_bio = am_first[0].biography;
	$("#artist_title").html(first_name);
	$("#artist_statement").html(first_bio);
}