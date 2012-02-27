from django import forms
from realestate.models import WoningObject

class SearchBox(forms.Form):
	
	def __init__(self):
		super(SearchBox, self).__init__()
		self.fields['location'] = forms.CharField(max_length=255)
		self.fields['price_from'] = forms.IntegerField()
		self.fields['price_till'] = forms.IntegerField()

	
	
