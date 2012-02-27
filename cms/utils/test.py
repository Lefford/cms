from django import forms

class TestForm(forms.ModelForm):
	class Meta:
		model = WoningObject
