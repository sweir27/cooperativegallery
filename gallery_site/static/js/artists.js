$(document).ready(function() {
	$("#main_artist_content").hide();
	display_main_artists();
	display_first_artist();
	generate_first_images();
	enableEvents();
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

function generate_first_images() {
	for (art in am_first) {
		artist = am_first[art].name
		artwork = JSON.parse(am_artwork[artist])

		if (artwork.length > 0) {
    		for (var a in artwork) {
    			if (typeof artwork[a].image != 'object') {
    				var url = '/media/'+artwork[a].image
    				var artist_id = artwork[a].artist_id
    				$("#all_artists").append("<div class='nailthumb-container square-thumb-larger all-thumbs' id='artist_"+artist_id+"'><img class='test_img' src='"+url+"'><div class='name-thumb' id='gray_artist_"+artist_id+"'>"+artist+"</div></img></div>")

    				break
    			}
    		}
    	}
	}

	$('.nailthumb-container').nailthumb({replaceAnimation:null});
}

function enableEvents() {

	$("body").on('click', '.artist_name', function(e) {
		$(".artist_name").css('color', 'black')
		$(this).css('color', 'gray')
		$("#all_artists").hide();
		$("#main_artist_content").show();
		var artist_name = $('> .artist_link', this).text();
		$("#artist_title").html('');
		$("#artist_title").html(artist_name);
		$("#artist_statement").html('');
		$(".thumbnails").html('');
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
	        				$(".thumbnails").append("<div class='nailthumb-container square-thumb ind-thumbs'><img class='test_img' src='"+url+"'></img></div>")
	        			}
	        		}
	        	}

	        	$('.nailthumb-container').nailthumb({replaceAnimation:null});
	        },
	        error: function (jqXHR, textStatus, errorThrown) {
		        // console.log(jqXHR.responseText);
		        // console.log(errorThrown)
		    }
	    });
	});

// $("body").on('mouseenter','.test_img', function(e) {
// 	console.log(this)
// 	var artist_id = 'gray_'+ $($(this).parent()).attr("id")
// 	// $('#'+artist_id).show();
// 	$(this).hide();
// });

	$(".test_img").mouseenter(function(){
		console.log("clicked")
		$(this).toggle();
	});

	// $(".test_img").mouseleave(function(){
	// 	console.log("out")
	// 	$(this).show();
	// });

}

