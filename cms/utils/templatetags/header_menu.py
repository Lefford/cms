from django.template import Library, Node
from django.contrib.flatpages.models import FlatPage

register = Library()

def header_menu():
        # All pages, discrimitate between actief and non - actief
        pages = FlatPage.objects.all()
           
        menu_header = "<ul class='left medium inverted-low horizontal'>"
        for page in pages:
                menu_header+="<li><a href='{0}'>{1}</a></li>".format(page.url, page.title)

        menu_header+='</ul>  '

        menu_header+="<ul class='right regular inverted-low horizontal'><li><a href='#'>English</a></ul>"
        

        return menu_header

register.simple_tag(header_menu)

