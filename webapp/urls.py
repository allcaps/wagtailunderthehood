from django.urls import re_path
from .views import serve


urlpatterns = [
    re_path(r'^((?:[\w\-]+/)*)$', serve),

]
