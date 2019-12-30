from django.contrib.gis import admin
from dam.models import Dam
from dam.models import DamCardDistributionPlace
from dam.models import DamType

admin.site.register(Dam, admin.OSMGeoAdmin)
admin.site.register(DamCardDistributionPlace, admin.OSMGeoAdmin)
admin.site.register(DamType, admin.OSMGeoAdmin)

