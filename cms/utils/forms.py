from django.forms import MultiValueField, FloatField, CharField
from cms.utils.widgets import LocationValueWidget

class LocationMultiValueFormField(MultiValueField):
	def __init__(self, fields=(), *args, **kwargs):
		fields = (
				CharField, 
				CharField,
				CharField, 
				CharField,
				FloatField,
				FloatField
		)

		if not kwargs.has_key('widget'):
			kwargs['widget'] = LocationValueWidget 
		super(LocationMultiValueFormField, self).__init__(fields=fields, *args, **kwargs)

	def compress(self, data_list):
		if data_list:
			return data_list
		return [None, None, None, None, 0,0, 0,0]

