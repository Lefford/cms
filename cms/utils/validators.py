from django.core.exceptions import ValidationError

def nl_zipcode(value):
	print 'nl_zipcode'

	if not value[:4].isdigit() or int(value[:4]) < 1000:
		raise ValidationError(u'{0} is not a valid zipcode'.format(value))

	
	return
