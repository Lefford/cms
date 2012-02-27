from django.contrib import admin
from django.contrib.flatpages.admin import FlatpageForm, FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.db import models

class ChildPage(FlatPage):
        child_of = models.ForeignKey('ChildPage', null=True, blank=True, default=None, related_name='parent_flatpage')
        show_after = models.ForeignKey('ChildPage', null=True, blank=True, default=None, related_name='predecessor_flatpage')

class ChildPageForm(FlatpageForm):
        class Meta:
                model = ChildPage
        
class ChildPageAdmin(FlatPageAdmin):
        form = ChildPageForm

        fieldsets = (
                        (None, {'fields': ('url', 'title', 'content', 'sites', 'show_after', 'child_of')}),
        )       

#admin.site.unregister(FlatPage)
admin.site.register(ChildPage, ChildPageAdmin)
