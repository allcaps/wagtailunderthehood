from django.contrib import admin
from django.urls import path, include

from webapp import urls as webapp_urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(webapp_urls))
]
