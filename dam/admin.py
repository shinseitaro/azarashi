from django.contrib.gis import admin

from dam.models import Dam
# Register your models here.
admin.site.register(Dam, admin.OSMGeoAdmin)