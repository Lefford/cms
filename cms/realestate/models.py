from django.db import models

# Create your models here.

def path_to_tumbs(instance, filename):
	return os.path.join('images','tumbs',str(instance.postcode), filename)

class WoningObject(models.Model):
	postcode = models.CharField(max_length=8)
	prijs = models.IntegerField()
	build_type = models.CharField(max_length=255)
	status = models.BooleanField()
	rooms = models.IntegerField()
	tumbs_pics = models.ImageField(upload_to=path_to_tumbs)
