#from django.contrib import admin
from django.contrib.gis import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from v1.views import DamViewSet, DamCardListViewSet, DamMapListViewSet
from card.views import CardViewSet

router = DefaultRouter()

router.register('dam/search', DamViewSet)

# cache 処理のために DamCardListViewSet を、ModelViewSet→ViewSetに変更したので、最後に basebaneオプションが必要になった
#router.register('dam/list', DamCardListViewSet)
router.register('dam/list', DamCardListViewSet, basename="dam/list")
router.register('dam/map', DamMapListViewSet, basename="dam/map")
router.register('card', CardViewSet, basename='card')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
