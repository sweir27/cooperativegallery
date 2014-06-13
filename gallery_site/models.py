from django.db import models
from django.utils import simplejson

# Create your models here.
class Artist(models.Model):
	name = models.CharField(max_length = 200)
	website = models.URLField(max_length = 200, null=True, blank=True)
	profile_pic = models.FileField(upload_to = 'profile_pics/', blank=True)
	biography = models.TextField(null=True, blank=True)
	added_at = models.DateTimeField(auto_now_add=True)

	def toJSON(self):
		return simplejson.dumps(self, default=dthandler, sort_keys=True)

class Artwork(models.Model):
	artist = models.ForeignKey(Artist)
	picture = models.FileField(upload_to = 'artists/%Y.%m.%d.%H.%M.%S', blank=True)
	description = models.TextField(null=True, blank=True)
	added_at = models.DateTimeField(auto_now_add=True)

class MainContent(models.Model):
	title = models.CharField(max_length = 200)
	description = models.TextField()
	picture = models.FileField(upload_to = 'mainpage/')
	added_at = models.DateTimeField(auto_now_add=True)

	def toJSON(self):
		return simplejson.dumps(self, default=dthandler, sort_keys=True)

def dthandler(obj):
    # lambda obj: obj.isoformat() if isinstance(obj, datetime.datetime) else obj.__dict__
    if hasattr(obj, 'isoformat'):
        return obj.isoformat()
    else:
        return obj.__dict__