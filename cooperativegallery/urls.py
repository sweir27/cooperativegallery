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

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
) 