import settings

from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cooperativegallery.views.home', name='home'),
    # url(r'^cooperativegallery/', include('cooperativegallery.foo.urls')),
    
    url(r'^$', 'gallery_site.views.index'),
    url(r'^contact/', 'gallery_site.views.contact'),
    url(r'^artists_main/', 'gallery_site.views.artists_main'),

    url(r'^upload_benoit_image/', 'gallery_site.views.upload_benoit_image'),
    url(r'^ajax_get_benoit_image/', 'gallery_site.views.ajax_get_benoit_image'),
    url(r'^get_benoit_image/', 'gallery_site.views.get_benoit_image'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
) 

if settings.DEBUG :
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )
