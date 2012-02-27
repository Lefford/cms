from django.db import models
from django.core.exceptions import ValidationError
from cms.utils.widgets import AutoCompleteWidget
from utils.validators import nl_zipcode
from cms.utils.forms import LocationMultiValueFormField

class LocationData(object):
	def __init__(self, address, zipcode, city, country, latitude, longtitude):
		self.address = address
		self.zipcode = zipcode
		self.city = city
		self.country = country
		self.longtitude = longtitude
		self.latitude = latitude

class LocationMultiValueField(models.Field):
	# Is needed to use Field.to_python method #
	__metaclass__ = models.SubfieldBase

	# Fix internationlization
	description = 'Address field for a object'

	def __init__(self, *args, **kwargs):
		super(LocationMultiValueField, self).__init__(*args, **kwargs)

	def to_pyhton(self, value):
		"""
		Converts a value returned from the database(or a serializer)
		and returns an Python object 
		"""
		if isinstance(value, LocationData):
			return value

		if isinstance(value, list):
			return LocationData(*value)

		if isinstance(value, basestring):
			return LocationData(value.split(','))
		
	def get_prep_value(self, value):
		"""
		This function does the reverse what the to_pyhton function does
		""" 
		
		return '{0},{1},{2},{4}'.format(value.address, value.zipcode, value.city, value.country, float(value.latitude), float(value.longtitude))

	def formfield(self, **kwargs):
		"""
		Field that represent a form field
		"""	

		defaults = {
				'form_class':	LocationMultiValueFormField,
		}
		
		defaults.update(kwargs)
	
		return super(LocationMultiValueField, self).formfield(**defaults)

	def get_internal_field(self):
		return 'LocationMultiValueField'

	def db_type(self, connection):
		if connection.settings_dict['ENGINE'] == 'django.db.mysyl':
			return 'text'

class AutoCompleteField(models.CharField):
	
	def formfield(self, **kwargs):
		""" 
		This field is needed to specify the form field(Already done by inheritance) for this model and let the form	
		initialze custom widget
		"""
		defaults = {'widget': AutoCompleteWidget}
		defaults.update(kwargs)

		return super(AutoCompleteField, self).formfield(**defaults)

class NLZipCodeField(models.CharField):
	def __init__(self, *args, **kwargs):
		kwargs['max_length'] = 6
	        kwargs['validators'] = [nl_zipcode]	
		super(NLZipCodeField, self).__init__(*args, **kwargs)

from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^cms\.utils\.models\.NLZipCodeField", "^cms\.utils\.models\.AutoCompleteField", "^cms\.utils\.models\.LocationMultiValueField"])
