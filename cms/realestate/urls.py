from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
	url(r'^huur/(?P<city>\w+)/$', 'realestate.views.search_house', name='search_city_house'),
	url(r'^huur/$', 'realestate.views.search_house', name='search_house'),
	url(r'^$', 'realestate.views.home', name='home'),
)
