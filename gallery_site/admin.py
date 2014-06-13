from django.contrib import admin
from gallery_site.models import Artist, Artwork, MainContent

# Register your models here.
admin.site.register(Artist)
admin.site.register(Artwork)
admin.site.register(MainContent)