#from django.contrib import admin
from django.contrib.gis import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from v1.views import DamViewSet

router = DefaultRouter()
router.register('dam', DamViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('card/', include('card.urls')),
]
