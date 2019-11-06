#from django.contrib import admin

from django.contrib.gis import admin 
from dam.models import Dam

admin.site.register(Dam, admin.OSMGeoAdmin)
