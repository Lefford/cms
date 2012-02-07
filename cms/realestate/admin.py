from django.contrib import admin
from realestate.models import WoningObject
from django import forms
from cms.utils.widgets import AutoCompleteWidget

class WoningAdminForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(WoningAdminForm, self).__init__(*args, **kwargs)
		self.fields['longitude'].widget.attrs['disabled'] = 'disabled'
		self.fields['latitude'].widget.attrs['disabled'] = 'disabled'
 
	class Meta:
		model = WoningObject
		widgets = {
			'adres': AutoCompleteWidget(),
			'street': AutoCompleteWidget()
		}
class WoningAdmin(admin.ModelAdmin):
	form = WoningAdminForm
	list_display = ('number', 'thumbnail', 'city', 'status')
	
admin.site.register(WoningObject, WoningAdmin)
