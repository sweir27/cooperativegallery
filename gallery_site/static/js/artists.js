$(document).ready(function() {
	$("#main_artist_content").hide();
	// display_main_artists();
	// display_first_artist();
	generate_first_images();
	enableEvents();
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

function display_first_artist() {
	var first_name = am_first[0].name;
	var first_bio = am_first[0].biography;
	var first_statement = am_first[0].artist_statement;
	$("#artist_title").html(first_name);
	$("#artist_statement").html(first_statement);
	$("#biography").html(first_bio);
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
    				$("#all_artists").append("<div class='nailthumb-container square-thumb-larger all-thumbs artist-image-thumb'"+ 
    					"id='artist_"+artist_id+"'><img class='test_img' src='"+url+"'>"+
    					"<div class='name-thumb' id='gray_artist_"+artist_id+"'>"+artist+
    					"</div></img></div>")

    				break
    			}
    		}
    	}
	}

	$('.nailthumb-container').nailthumb({replaceAnimation:null});
}

function clickArtist(link) {
	$(".artist_name").css('color', 'black')
	$(link).css('color', '#B03060')
	$("#all_artists").hide();
	$("#main_artist_content").show();
	var artist_name = $('> .artist_link', link).text();
	$("#artist_title").html('');
	$("#artist_title").html(artist_name);
	$("#website").html('');
	$("#artist_statement").html('');
	$(".thumbnails").html('');
	$(".main_pic_wrapper").html('');
	$("#statement_title").show();
	$("#bio_title").show();
	$("#website").show();

	$.ajax({
        url: "/ajax_get_artist_image/",
        type: "POST",
        data: { 
        	name: artist_name,
        	csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value 
        },
        success: function(data) {
        	var artist = JSON.parse(data["artist"])
        	var website = artist[0].website
        	if (typeof artist[0].artist_statement != 'object') {
        		$("#artist_statement").html(artist[0].artist_statement);
        	} else {
        		$("#statement_title").hide();
        	}

        	if (typeof artist[0].biography != 'object') {
        		$("#biography").html(artist[0].biography);
        	} else {
        		$("#bio_title").hide();
        	}

        	if (typeof website != 'object') {
        		$("#website").append("<a id='website_link' href='"+website+"'>"+website+"</a>");
        	} else {
        		$("#website").hide();
        	}

        	//generate thumbnails
        	var artwork = JSON.parse(data["artwork"])
        	if (artwork.length > 0) {
        		for (var a in artwork) {
        			if (typeof artwork[a].image != 'object') {
        				var url = '/media/'+artwork[a].image
        				var artwork_id = artwork[a].id
        				$(".thumbnails").append("<div class='nailthumb-container square-thumb ind-thumbs'>"+
        					"<img class='ind_img' id='thumb_id_"+artwork_id+"' src='"+url+"'></img></div>")
        			}
        		}
        	}

        	//generate first main picture
        	if (artwork.length > 0) {
	    		for (var a in artwork) {
	    			if (typeof artwork[a].image != 'object') {
	    				var url = '/media/'+artwork[a].image
	    				var artist_id = artwork[a].artist_id
	    				var artwork_id = artwork[a].id
	    				$(".main_pic_wrapper").append("<div class='main_pic' id='main_art_"+artwork_id+"'><img class='main_img' src='"+url+"'></img></div>")

	    				break
	    			}
	    		}
	    	}

        	$('.nailthumb-container').nailthumb({replaceAnimation:null});

        	//wrap each image with a link to enable the slideshow
        	$('img.ind_img').each(function(){
	            var artwork_id = $(this).attr('id').split('thumb_id_')[1]
	            for (var a in artwork) {
	            	if (artwork[a].id == artwork_id) {
						// var url = '/media/'+artwork[a].image
						// var artist_id = artwork[a].artist_id
						var title = artwork[a].title
					}
	            }
	            $(this).wrap('<a href="'  + $(this).attr('src') +
                  '" title="' + title +
                  '" rel=lightbox_show></a>');
	        });

        	//enable slideshow
	        $("a[rel^='lightbox']").slimbox({
	        	// loop: true,
	        }); 
        },
        error: function (jqXHR, textStatus, errorThrown) {
	        // console.log(jqXHR.responseText);
	        // console.log(errorThrown)
	    }
    });
}

function changeMainPic(artwork_id) {
	var artist = $("#artist_title").html()
	artwork = JSON.parse(am_artwork[artist])
	$(".main_pic_wrapper").html('')
	// console.log('pre artwork id '+artwork_id)
	for (var a in artwork) {
		// console.log('artwork '+artwork[a].id)
		if (artwork[a].id == artwork_id) {
			var url = '/media/'+artwork[a].image
			var artist_id = artwork[a].artist_id
			$(".main_pic_wrapper").append("<div class='main_pic' id='main_art_"+artwork_id+
				"'><img class='main_img' src='"+url+"'></img></div>")
		}
	}
	
}

function enableEvents() {

	$("body").on('click', '.artist_name', function(e) {
		console.log(this)
		clickArtist(this);
	});

	$(".artist-image-thumb").hover(
		function(){
			$(this).find('.test_img').hide();
		},
		function(){
			$(this).find('.test_img').show();
	});

	$(".test_img").mouseenter(function(){
		//$(this).toggle();
	});

	$(".name-thumb").mouseenter(function(){
		// $(this).toggle();
		console.log($(this).parent())
	});

	//Does nothing right now... but maybe later when the hover thing is fixed
	$("body").on('click', '.test_img', function(e) {
		var id = $(this).attr('id').split('gray_artist_')[1]
		var el = $('#name_'+id);
		clickArtist(el)
	});

	$("body").on('click', '.name-thumb', function(e) {
		var id = $(this).attr('id').split('gray_artist_')[1]
		var el = $('#name_'+id);
		clickArtist(el)
	});

	$("body").on('click', '.ind_img', function(e) {
		var artwork_id = $(this).attr('id').split('thumb_id_')[1]
		changeMainPic(artwork_id)
	});

}

