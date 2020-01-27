from rest_framework import generics, viewsets
from rest_framework_gis.filters import DistanceToPointFilter
from rest_framework_gis.pagination import GeoJsonPagination
from rest_framework.pagination import PageNumberPagination
from django_filters import rest_framework as filters
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from django.db.models import Count, F, Q
from dam.models import Dam
from v1.serializers import (DamGeoFeatureModelSerializer, DamCardSerializer, DamMapModelSerializer, DamIdSerializer,
                            DamCountSerializer, DamCardDistributionPlaceSerializer, DamStatsSerializer)
from django.shortcuts import get_object_or_404
from decimal import Decimal

class GeojsonLocationList(generics.ListCreateAPIView):
    pagination_class = GeoJsonPagination


class DamPagination(PageNumberPagination):
    # url のリクエスト　例：GET /api/dam/?page=2
    page_size_query_param = 'page_size'
    # 一ページあたりの件数
    page_size = 12


class DamFilter(filters.FilterSet):
    # この変数名が、 url のクエリ文字列キーになる
    # 例: `api/dam/?prefecture=愛知`
    prefecture = filters.CharFilter(field_name='prefecture', lookup_expr='contains')
    river = filters.CharFilter(field_name='river_name', lookup_expr='contains')
    water_system = filters.CharFilter(field_name='water_system_name', lookup_expr='contains')
    name = filters.CharFilter(field_name='name', lookup_expr='contains')
    address = filters.CharFilter(field_name='address', lookup_expr='contains')
    total_pondage = filters.CharFilter(field_name='total_pondage', lookup_expr='gt')

    class Meta:
        model = Dam
        fields = ("name", "address",)


class DamIdFilter(filters.FilterSet):
    dam_code = filters.NumberFilter(field_name='dam_code')

    class Meta:
        model = Dam
        fields = ( )

class DamBaseStatsViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'head',]


class DamViewSet(viewsets.ModelViewSet):
    queryset = Dam.objects.all()
    serializer_class = DamGeoFeatureModelSerializer
    pagination_class = DamPagination
    filter_backends = (filters.DjangoFilterBackend, DistanceToPointFilter,)  #
    distance_filter_field = 'geom'
    distance_filter_convert_meters = True
    filterset_class = DamFilter


class DamTopTotalPondageView(DamBaseStatsViewSet):
    queryset = Dam.objects.filter(scale_bank_height__gt=Decimal(0)).order_by('-total_pondage').extra(
        select={'rank': 'RANK() OVER(ORDER BY total_pondage DESC)'})[:10]
    serializer_class = DamStatsSerializer


class DamBottomTotalPondageView(DamBaseStatsViewSet):
    queryset = Dam.objects.filter(Q(scale_bank_height__gt=Decimal(0)) & Q(total_pondage__gt=0)).order_by('total_pondage').extra(
        select={'rank': 'RANK() OVER(ORDER BY total_pondage DESC)'})[:10]
    serializer_class = DamStatsSerializer


class DamTopCountByPrefectureView(DamBaseStatsViewSet):
    serializer_class = DamCountSerializer

    def get_queryset(self):
        key = 'prefecture'
        queryset = Dam.objects.values(key).annotate(count=Count(key)).order_by('-count')
        return queryset


class DamIdViewSet(DamViewSet):
    serializer_class = DamIdSerializer


class DamCardListViewSet(viewsets.ModelViewSet):
    # issue_84 で、ページネーションを使うことにした
    queryset = Dam.objects.order_by(F('card__published_date').desc(nulls_last=True))
    serializer_class = DamCardSerializer
    pagination_class = DamPagination


class DamMapListViewSet(viewsets.ViewSet, APIView):
    permission_classes = (AllowAny,)

    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_cookie)
    def list(self, request):
        queryset = Dam.objects.all()
        serializer = DamMapModelSerializer(queryset, many=True)
        return Response(serializer.data)


class DamCardDistributionPlaceViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = DamCardDistributionPlaceSerializer

    def get_queryset(self):
        dam_id = self.kwargs.get('dam_id')
        dam = get_object_or_404(Dam, pk=dam_id)
        queryset = dam.card_distribution_places.all()
        return queryset
