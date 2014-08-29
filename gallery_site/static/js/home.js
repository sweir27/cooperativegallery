$(document).ready(function() {
	display_main_content();
});

function display_main_content() {
	$(".show_images_one").show();
	$(".show_images_two").hide();
	$("#thursday_section_title").hide()
	var title = mc_first[0].title;
	var description = mc_first[0].description
	var artists = mc_first[0].artists
	var start = mc_first[0].show_start
	var end = mc_first[0].show_end

	var thursday_title = mc_first[0].thursday_title
	var thursday_description = mc_first[0].thursday_description
	var thurs_time_pre = mc_first[0].thursday_time

	var month_dict = {'01':'January',
						'02':'February',
						'03':'March',
						'04':'April',
						'05':'May',
						'06':'June',
						'07':'July',
						'08':'August',
						'09':'September',
						'10':'October',
						'11':'November',
						'12':'December',
	}

	var start_month = month_dict[start.split('-')[1]]
	var start_day = start.split('-')[2]
	var start_year = start.split('-')[0]

	var end_month = month_dict[end.split('-')[1]]
	var end_day = end.split('-')[2]
	var end_year = end.split('-')[0]

	if (typeof thurs_time_pre != 'object') {
		var thurs_month = month_dict[thurs_time_pre.split('-')[1]]
		var thurs_day = thurs_time_pre.split('T')[0].split('-')[2]
		var thurs_year = thurs_time_pre.split('-')[0]
		var thurs_time = thurs_time_pre.split('T')[1].split('+')[0].substring(0,5)
		$("#thursday_time").html(thurs_month+" "+thurs_day+", "+thurs_year+" at "+thurs_time)
	}

	console.log(mc_first[0].image_1)
	console.log(mc_first[0].image_2)

	if (mc_first[0].image_2 == "") {
		$(".show_images_two").hide();
		var url = '/media/'+mc_first[0].image_1
		$("#center_img").attr('src', url)
	} else {
		$(".show_images_one").hide();
		$(".show_images_two").show();
		var url_1 = '/media/'+mc_first[0].image_1
		var url_2 = '/media/'+mc_first[0].image_2
		$("#left_img").attr('src', url_1)
		$("#right_img").attr('src', url_2)
	}

	$("#show_title").html(title);
	$("#show_description").html(description);
	$("#show_artists").html("Artists: "+artists)
	$("#show_time").html(start_month+" "+start_day+", "+start_year+ " to "+end_month+" "+end_day+", "+end_year)

	if (thursday_title != "") {
		$("#thursday_section_title").show()	
		$("#thursday_title").html(thursday_title)
		$("#thursday_description").html(thursday_description)
	}



}