from django.db import models
import os
from cms.utils.models import AutoCompleteField, NLZipCodeField
from cms.utils.validators import nl_zipcode
from cms.settings import PROJECT_ROOT
# Create your models here.

def path_to_tumbs(instance, filename):

	return os.path.join('images', str(instance.city), str(instance.zip_code), str(instance.number), str(instance.extension) ,'thumbs', filename)

class Address(models.Model):

	street		= models.CharField(max_length=255)
	zip_code	= NLZipCodeField()
	number		= models.IntegerField()
	extension	= models.CharField(max_length=3)
	city 		= models.CharField(max_length=31)
	adres		= AutoCompleteField(max_length=255)

	class Meta:
		abstract = True

class WoningObject(Address):
	prijs = models.IntegerField()
	build_type = models.CharField(max_length=255)
	status = models.BooleanField()
	rooms = models.IntegerField()
	tumbs_pics = models.ImageField(upload_to=path_to_tumbs)
	latitude = models.FloatField(blank=True, null=True)
	longitude = models.FloatField(blank=True, null=True)

	def thumbnail(self):
		return """<img border="0" alt="" src="/media/{0}" height="40" />""".format(self.tumbs_pics)
	thumbnail.allow_tags = True
