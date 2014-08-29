from django.db import models
from django.utils import simplejson
from django.forms import ModelForm
from django.contrib.auth.models import User

# Create your models here.
class Artist(models.Model):
	name = models.CharField(max_length = 200)
	website = models.URLField(max_length = 200, null=True, blank=True)
	profile_pic = models.FileField(upload_to = 'profile_pics', blank=True)
	biography = models.TextField(null=True, blank=True)
	artist_statement = models.TextField(null=True, blank=True)
	added_at = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(User, default=1, null=True)

	def __unicode__(self):
		return self.name
	def toJSON(self):
		return simplejson.dumps(self, default=dthandler, sort_keys=True)

class Artwork(models.Model):
	artist = models.ForeignKey(Artist)
	image = models.FileField(upload_to = 'artists', null=True)
	title = models.CharField(max_length = 200, blank=True, null=True)
	# description = models.TextField(null=True, blank=True)
	added_at = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.title
	def toJSON(self):
		return simplejson.dumps(self, default=dthandler, sort_keys=True)

class MainContent(models.Model):
	title = models.CharField(max_length = 200)
	artists = models.CharField(max_length = 200, help_text="Input one or more artists with commas in between (i.e. 'Joe Shmo, John Smith')")
	description = models.TextField()
	image_1 = models.FileField(upload_to = 'mainpage', null=True)
	image_2 = models.FileField(upload_to = 'mainpage', null=True, blank=True)
	show_start = models.DateField()
	show_end = models.DateField()
	thursday_title = models.CharField(max_length = 200, help_text="(Optional)", null=True, blank=True)
	thursday_description = models.TextField(help_text="(Optional)", null=True, blank=True)
	thursday_time = models.DateTimeField(null=True, blank=True, help_text='(Optional)')
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

class Migration:

    def forwards(self, orm):
        # Rename 'name' field to 'full_name'
        db.rename_column('gallery_site_maincontent', 'name', 'full_name')

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
