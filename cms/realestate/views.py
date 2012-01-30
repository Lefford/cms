from django.http import HttpResponse
# Create your views here.

def home(request):
	return HttpResponse('Homemade', status=201)

def search_house(request, city=None):
	response = ''
	if city:
		response = 'Found city {0}'.format(city) 
	
	return HttpResponse(response)

