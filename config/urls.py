#from django.contrib import admin
from django.contrib.gis import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter

from v1.views import DamViewSet, DamCardListViewSet, DamMapListViewSet

router = DefaultRouter()
# dam/list で、
router.register('dam/search', DamViewSet)
router.register('dam/list', DamCardListViewSet)
router.register('dam/map', DamMapListViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/card/', include('card.urls')),
    path('auth/', include('rest_framework_social_oauth2.urls')),
    re_path('^(?:.*)/?', include('frontend.urls')),
]
