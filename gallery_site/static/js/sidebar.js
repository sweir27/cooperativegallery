$(document).ready(function() {
	display_main_artists();
});

function display_main_artists() {
	for (a in am_first) {
		var name = am_first[a].name;
		var biography = am_first[a].biography;
		var statement = am_first[a].artist_statement;
		var id = am_first[a].id;

		var artist_el = "<li class='artist_name' id='name_"+id+"'><div class='artist_link'>"+name+"</div></li>";
		$("#artists_list").append(artist_el);
	}
}