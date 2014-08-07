from django.contrib import admin
from gallery_site.models import Artist, Artwork, MainContent

# @admin.register(Artwork)
# class ArtworkAdmin(admin.ModelAdmin):
# 	pass

class ArtworkAdmin(admin.ModelAdmin):

    def queryset(self, request):
        """Limit Artwork to those that belong to the request's user."""
        qs = super(ArtworkAdmin, self).queryset(request)
        if request.user.is_superuser:
            # It is mine, all mine. Just return everything.
            return qs
        # Now we just add an extra filter on the queryset and
        # we're done. Assumption: Artwork.owner is a foreignkey
        # to a User.
        artist_user = Artist.objects.filter(owner=request.user)
        return qs.filter(artist=artist_user)

    fieldsets = ((None, {'fields': ('artist', 'image', 'title')}),)
    restricted_fieldsets = ((None, {'fields': ('image', 'title')}),)

    def get_fieldsets(self, request, obj=None):
	    if not request.user.is_superuser:
	        return self.restricted_fieldsets
	    else:
	        return super(ArtworkAdmin, self).get_fieldsets(request, obj=obj)

    def save_model(self, request, obj, form, change):
		artist_user = Artist.objects.filter(owner=request.user)
		if not request.user.is_superuser:
			obj.artist = author_user
		obj.save()


# Register your models here.
admin.site.register(Artist)
admin.site.register(Artwork, ArtworkAdmin)
admin.site.register(MainContent)

