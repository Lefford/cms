from django.forms import TextInput, MultiWidget
from django.utils.safestring import mark_safe
import re

class AutoCompleteWidget(TextInput):
	class Media:
		css = {
			'all': ('/static/utils/css/jquery-ui-1.8.17.custom.css',)
		}

		js = (
			('/static/utils/js/jquery.js', '/static/utils/js/jquery-ui-1.8.17.custom.min.js',)
		)

	def __init__(self, attrs=None, *args, **kwargs):
		url =  kwargs.pop('url', 'autocomplete')
		self.url = url
		print url
		super(AutoCompleteWidget, self).__init__(attrs)

	def render(self, name, value, attrs):
		html = super(AutoCompleteWidget, self).render(name, value, attrs)
		return html + mark_safe(
						u"""	<script>
						    		$( '#%s' ).autocomplete({
	        					                source: function( request, response ) {
					        	                        $.ajax({
						                                        url: "%s",
						                                        dataType: "JSON",
						                                        data: {address: request.term},
						                                        success: function( data ) {
                                             							response( $.map( data.results, function( value ) {
														var latitude	  = value.geometry.location.lat;
														var longtitude 	  = value.geometry.location.lng;
														
														var arr = [value.formatted_address , latitude, longtitude]

														addressValue = arr.join(',');
														console.log(addressValue);
						                                                      return {
                                                						              label: a,
						                                                              value: value.formatted_address
                                                							      }
							                                         }));
                                        						}
                                						});
	                        					},
						                        minLength: 2,
        						        });             
						 	</script>
						""" % (attrs['id'], self.url)
					)
class LocationValueWidget(MultiWidget):
	def __init__(self, attrs=None, **kwargs):
		widgets = [TextInput(attrs={'name': 'hallo'}), TextInput, TextInput, TextInput, TextInput, TextInput]
		super(LocationValueWidget, self).__init__(widgets, attrs, **kwargs)

	def decompress(self, value):
		if value:
			return [value.address, value.zipcode, value.city, value.country, value.latitude, value.longtitude]
		return [None, None, None, None, None, None]

	def format_output(self, rendered_widgets):
		"""
		    Given a list of rendered widgets (as strings), returns a Unicode string
		    representing the HTML for the whole lot.
	
		    This hook allows you to format the HTML design of the widgets, if needed.		
		"""
		print rendered_widgets 
		print '#' * 29
		id_widget=re.compile('id_(\w+)_[0-9]+')
		
		try:
			aa = map(lambda x: id_widget.search(x), [i for i in rendered_widgets])
		except AttributeError: 
			print 'No id founded for {0}'.format(i)

		a = 0
		label_names = ['Address', 'Zipcode', 'City', 'Country', 'Latitude', 'Longtitude']
		for i, value in enumerate(aa):
			if a > 0:
				a = a+ 1 
	
			rendered_widgets.insert(a, "<label for='{0}'>{1}</label>".format(value.group(), label_names[i]))
			a = a+2
			rendered_widgets.insert(a, "<br />")
			print rendered_widgets
		return u''.join(rendered_widgets)
		
