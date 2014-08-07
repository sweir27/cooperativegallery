from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext, loader
from django.utils import simplejson
from gallery_site.models import Artist, Artwork, MainContent, BenoitImage, BenoitImageForm
from django.core.urlresolvers import reverse
from django.http import HttpResponse

# Create your views here.

def model_to_json(instances):
    result = []
    # Hack to serialize a django model. There is no good way to deal with foreign keys.
    for instance in instances:
        result.append(simplejson.loads(instance.toJSON()))
    return simplejson.dumps(result)

# def index(request):
# 	return render_to_response('index.html', locals(), context_instance = RequestContext(request))

def index(request):
	content = MainContent.objects.all().order_by('-added_at')
	
	#TODO check for none
	recent_con = content[0]

	print recent_con.title

	return render(
		request, 
		"index.html",
		{
			'content': model_to_json([recent_con])
		}
	)

def contact(request):
	artists = Artist.objects.all().order_by('name')

	return render(
		request, 
		"contact.html",
		{
			'artists': model_to_json(artists),
		}
	)

def artists_main(request):
	artists = Artist.objects.all().order_by('name')
	artwork = {}
	for a in artists:
		#Add in functionality if artwork is deselected
		art = Artwork.objects.filter(artist=a)
		artwork[a.name] = model_to_json(art)

	print artwork

	# response = {
		# 	'artists': model_to_json(artists),
		# 	'artwork': artwork
		# }

	return render(
		request, 
		"artists_main.html",
		{
			'artists': model_to_json(artists),
			'artwork': simplejson.dumps([artwork])
		}
	)

# def artist(request):
# 	return render_to_response('artists_main.html', locals(), context_instance = RequestContext(request))

def upload_benoit_image(request):
    if request.method == 'POST':
        form = BenoitImageForm(request.POST, request.FILES)
        if form.is_valid():
            new_benoit_image = form.save()
            return HttpResponse('the file was uploaded on your drive at %s and was save in your database under the title %s' % (new_benoit_image.image.url,new_benoit_image.title))
    else:
        form = BenoitImageForm()
    return render(request, 'upload_benoit_image.html', {'form': form})

def ajax_get_benoit_image(request):
    title = request.POST.get('title')
    benoit_image = get_object_or_404(BenoitImage, title=title)
    print benoit_image.image.url
    response = { 'title': benoit_image.title, 'size': benoit_image.image.size, 'url': benoit_image.image.url }
    return HttpResponse(simplejson.dumps(response))

def get_benoit_image(request):
    return render(request, 'get_benoit_image.html')

def ajax_get_artist_image(request):
	print 'HERE'
	name = request.POST['name']
	print name
	artist = Artist.objects.filter(name=name)
	print artist

	artwork = Artwork.objects.filter(artist=artist)
	print artwork

	# if (len(artwork) > 0):
		# print artwork[2].image
	response={
		'name':name, 
		'artist':model_to_json(artist), 
		'artwork':model_to_json(artwork),
	}
	return HttpResponse(simplejson.dumps(response), mimetype='application/json')

# def artist_upload_image(request):
#     if request.method == 'POST':
#         form = ArtworkForm(request.POST, request.FILES)
#         if form.is_valid():
#             new_image = form.save()
#             return HttpResponse('the file was uploaded on your drive at %s and was save in your database under the title %s' % (new_image.image.url,new_image.title))
#     else:
#         form = ArtworkForm()
#     return render(request, 'artist_upload_image.html', {'form': form})
