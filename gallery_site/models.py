from django.db import models
from django.utils import simplejson
from django.forms import ModelForm

# Create your models here.
class Artist(models.Model):
	name = models.CharField(max_length = 200)
	website = models.URLField(max_length = 200, null=True, blank=True)
	profile_pic = models.FileField(upload_to = 'profile_pics', blank=True)
	biography = models.TextField(null=True, blank=True)
	added_at = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.name

	def toJSON(self):
		return simplejson.dumps(self, default=dthandler, sort_keys=True)

class Artwork(models.Model):
	artist = models.ForeignKey(Artist)
	image = models.FileField(upload_to = 'artists', null=True)
	title = models.CharField(max_length = 200, blank=True, null=True)
	description = models.TextField(null=True, blank=True)
	added_at = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.title

class MainContent(models.Model):
	title = models.CharField(max_length = 200)
	description = models.TextField()
	picture = models.FileField(upload_to = 'mainpage')
	added_at = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.title

	def toJSON(self):
		return simplejson.dumps(self, default=dthandler, sort_keys=True)

class BenoitImage(models.Model):
	title = models.CharField(max_length = 200)
	image = models.FileField(upload_to = 'benoit_images')

class BenoitImageForm(ModelForm):
	class Meta:
		model = BenoitImage
		fields = ['title','image']

# class ArtworkForm(ModelForm):
# 	class Meta:
# 		model = Artwork
# 		fields = ['artist','image','title','description']

def dthandler(obj):
    # lambda obj: obj.isoformat() if isinstance(obj, datetime.datetime) else obj.__dict__
    if hasattr(obj, 'isoformat'):
        return obj.isoformat()
    else:
        return obj.__dict__
