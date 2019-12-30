#from django.contrib import admin
from django.contrib.gis import admin
from dam.models import Dam
from dam.models import DamCardDistributionPlace
from dam.models import DamType

admin.site.register(Dam, admin.OSMGeoAdmin)
admin.site.register(DamCardDistributionPlace, admin.OSMGeoAdmin)
admin.site.register(DamType, admin.OSMGeoAdmin)
# @admin.site.register(Dam)
# class DamAdmin(admin.OSMGeoAdmin):
#     model = Dam
#     search_fields = ('name', )

