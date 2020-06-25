from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.http import Http404
from django.shortcuts import render
from treebeard.mp_tree import MP_Node


class Site(models.Model):
    name = models.CharField(max_length=255)
    domain = models.CharField(max_length=255)
    root_page = models.ForeignKey("Page", on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Page(MP_Node):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    live = models.BooleanField(default=True)
    content_type = models.ForeignKey(
        ContentType,
        related_name='pages',
        on_delete=models.PROTECT,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.id:
            self.content_type = ContentType.objects.get_for_model(self)

    def __str__(self):
        return self.title

    @property
    def specific(self):
        content_type = ContentType.objects.get_for_id(self.content_type_id)
        return content_type.get_object_for_this_type(id=self.id)

    def serve(self, request):
        return render(request, f"webapp/{self.__class__.__name__.lower()}.html", {"page": self})

    def route(self, request, slugs):
        if slugs:
            child_slug = slugs[0]
            remaining_slugs = slugs[1:]

            try:
                subpage = self.get_children().get(slug=child_slug)
            except Page.DoesNotExist:
                raise Http404

            return subpage.specific.route(request, remaining_slugs)

        else:
            if self.live:
                return self.serve(request)
            else:
                raise Http404


class HomePage(Page):
    intro = models.TextField()


class BlogPage(Page):
    author = models.CharField(max_length=255)
    body = models.TextField()
