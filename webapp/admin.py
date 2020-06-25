from .models import Site, Page, HomePage, BlogPage
from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory


class PageAdmin(TreeAdmin):
    form = movenodeform_factory(Page)


admin.site.register(Page, PageAdmin)
admin.site.register(HomePage)
admin.site.register(BlogPage)
admin.site.register(Site)
