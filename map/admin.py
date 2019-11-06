# from django.contrib import admin
from django.contrib.gis import admin
from map.models import Hoikusho

admin.site.register(Hoikusho, admin.OSMGeoAdmin)



