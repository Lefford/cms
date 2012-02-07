from django.conf.urls.defaults import patterns, include, url
from realestate.views import GoogleMapsView, TestGoogleView

urlpatterns = patterns('',
	url(r'^huur/(?P<city>\w+)/$', 'realestate.views.search_house', name='search_city_house'),
	url(r'^huur/$', 'realestate.views.search_house', name='search_house'),
	url(r'^$', 'realestate.views.home', name='home'),
	url(r'^google-maps/$', GoogleMapsView.as_view()),
	url(r'test-maps/$', TestGoogleView.as_view()),
	url(r'^admin/realestate/\w+/.+/autocomplete/$', 'realestate.views.google_geo_code', name='geocode'),	
	url(r'^places/$', 'realestate.views.google_geo_code'),
)
