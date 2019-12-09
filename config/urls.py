#from django.contrib import admin
from django.contrib.gis import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter 

from v1.views import DamViewSet, DamCardlistViewSet

router = DefaultRouter()
# dam/list で、
router.register('dam', DamViewSet)
router.register('list', DamCardlistViewSet)




urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
