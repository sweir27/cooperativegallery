$(document).ready(function() {
	display_main_content();
});

function display_main_content() {
	var title = mc_first[0].title;
	var description = mc_first[0].description
	$("#show_title").html(title);
	$("#show_description").html(description);
}