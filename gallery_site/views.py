from django.shortcuts import render, render_to_response
from django.template import RequestContext, loader
from django.utils import simplejson
from gallery_site.models import Artist, Artwork, MainContent
from django.core.urlresolvers import reverse

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
			# 'content':'hello!'
		}
	)

def contact(request):
	return render(
		request, 
		"contact.html"
	)

def artists_main(request):
	artists = Artist.objects.all().order_by('name')
	return render(
		request, 
		"artists_main.html",
		{
			'artists': model_to_json(artists)
		}
	)

# def artist(request):
# 	return render_to_response('artists_main.html', locals(), context_instance = RequestContext(request))


