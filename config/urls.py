# from django.contrib import admin
from django.contrib.gis import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
