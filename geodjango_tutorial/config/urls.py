# from django.contrib import admin
from django.contrib.gis import admin
from django.urls import path, include 
from rest_framework.routers import DefaultRouter 

from world.views import SchoolViewSet, FacilityViewSet, BusstopViewSet

router = DefaultRouter()
router.register('school', SchoolViewSet)
router.register('facility', FacilityViewSet)
router.register('busstop', BusstopViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
	path('api/', include(router.urls))
]

