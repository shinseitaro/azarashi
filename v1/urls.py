from rest_framework import routers

from v1.views import (DamViewSet, DamCardListViewSet, DamMapListViewSet, DamIdViewSet,
                      DamTopTotalpontageView, DamBottomTotalpontageView, DamTopCountByPrefectureView,
                      DamCardDistributionPlaceViewSet)
from card.views import CardViewSet

router = routers.DefaultRouter()

# cache 処理のために DamCardListViewSet を、ModelViewSet→ViewSetに変更したので、最後に basebaneオプションが必要になった
router.register('dam/search', DamViewSet, basename="dam/search")
router.register('dam/list', DamCardListViewSet, basename="dam/list")
router.register('dam/top_totalpontage', DamTopTotalpontageView, basename="dam/top_totalpontage")
router.register('dam/bottom_totalpontage', DamBottomTotalpontageView, basename="dam/bottom_totalpontage")
router.register('dam/top_by_pref', DamTopCountByPrefectureView, basename="dam/top_by_pref")
router.register('dam/map', DamMapListViewSet, basename="dam/map")
router.register('card', CardViewSet, basename='card')
router.register('dam/(?P<dam_id>[0-9]+)/distribution', DamCardDistributionPlaceViewSet, basename="dam/card_distribution_place")
router.register('dam', DamIdViewSet, basename='dam')
urlpatterns = router.urls
