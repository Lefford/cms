from django.http import HttpResponse
from django.views.generic import TemplateView
from django.http import HttpResponseForbidden

import urllib
import simplejson

GOOGLE_GEO_URL = 'http://maps.googleapis.com/maps/api/geocode'

# Create your views here.

def home(request):
	return HttpResponse('Homemade', status=201)

def search_house(request, city=None):
	response = ''
	if city:
		response = 'Found city {0}'.format(city) 
	
	return HttpResponse(response)

class GoogleMapsView(TemplateView):
	template_name = 'google-maps.html'

class TestGoogleView(TemplateView):
	template_name = 'maps-test.html'

def google_geo_code(request, address=None):
	output = request.META['HTTP_ACCEPT']
	address = request.GET.get('address','')
	message = ''

	if 'json' in output:
		output_type = '/json?'
	elif 'xml' in output:
		output_type = '/xml?'
	else:
		message = '{0} format not supported'.format(output)
		return HttpResponseForbidden(message)

	if address:
		param = urllib.urlencode({'address': address, 'sensor': 'false'})
		search_string = '{0}{1}{2}'.format(GOOGLE_GEO_URL, output_type, param) 
		print search_string
		result = simplejson.load(urllib.urlopen(search_string))
		print result
		if result:	
			message = simplejson.dumps(result, indent=2)

	return HttpResponse(message, content_type='JSON')
		 
