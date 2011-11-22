from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from navigation.views import list_all

admin.autodiscover()

urlpatterns = patterns('',
    # Examples: 
    # url(r'^$', 'openbrain.views.home', name='home'),
    # url(r'^openbrain/', include('openbrain.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^list/', list_all)

    # url(r'^(.*)/', category
    # url(r'^(.*)/(.*)/', category, topic,
)
