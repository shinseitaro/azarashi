#from django.contrib import admin
from django.contrib.gis import admin 
from world.models import School, Facility, Busstop
from leaflet.admin import LeafletGeoAdmin # 追加

# マップ表示
# admin.site.register(School, admin.GeoModelAdmin)
# admin.site.register(Facility, admin.GeoModelAdmin)
# admin.site.register(Busstop, admin.GeoModelAdmin)

# Open StreetMap 表示
# admin.site.register(School, admin.OSMGeoAdmin)
# admin.site.register(Facility, admin.OSMGeoAdmin)
# admin.site.register(Busstop, admin.OSMGeoAdmin)


class SchoolAdmin(LeafletGeoAdmin):
  search_fields = ['a27_001','a27_002','a27_003', 'a27_004']
  list_filter = ('a27_002')

admin.site.register(School, LeafletGeoAdmin)
admin.site.register(Facility, LeafletGeoAdmin)
admin.site.register(Busstop, LeafletGeoAdmin)