from django.shortcuts import render
from rest_framework import generics,viewsets

from rest_framework_gis.filters import DistanceToPointFilter
from rest_framework_gis.pagination import GeoJsonPagination
from rest_framework.pagination import PageNumberPagination
from django_filters import rest_framework as filters
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAuthenticated

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from django.db.models import Count

from dam.models import Dam
from v1.serializers import (DamGeoFeatureModelSerializer, DamSerializer, DamListSerializer, DamCardListSerializer,
                            DamCardSerializer, DamMapModelSerializer, DamIdSerializer, DamCountSerializer)

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
        fields = ("name", "address", )


class DamIdFilter(filters.FilterSet):
    dam_code = filters.NumberFilter(field_name='dam_code')
    class Meta:
        model = Dam
        fields = ( )

class DamViewSet(viewsets.ModelViewSet):

    queryset = Dam.objects.all()
    serializer_class = DamGeoFeatureModelSerializer
    pagination_class = DamPagination
    filter_backends = (filters.DjangoFilterBackend,DistanceToPointFilter,) #
    distance_filter_field = 'geom'
    distance_filter_convert_meters = True
    filterset_class = DamFilter
    http_method_names = ['get', 'head', 'option']


class DamTopTotalpontageView(DamViewSet):
    queryset = Dam.objects.all().order_by('-total_pondage')
    serializer_class = DamCardSerializer


class DamBottomTotalpontageView(DamTopTotalpontageView):
    queryset = Dam.objects.all().order_by('total_pondage')


class DamTopCountByPrefectureView(DamTopTotalpontageView):
    serializer_class = DamCountSerializer

    def get_queryset(self):
        key = 'prefecture'
        queryset = Dam.objects.values(key).annotate(count=Count(key)).order_by('-count')
        #print(queryset)
        # QuerySet [{'prefecture': '北海道', 'count': 190}, {'prefecture': '岡山県', 'count': 166}, {'prefecture': '新潟県', 'count': 114}, {'prefecture': '兵庫県', 'count': 104}, {'prefecture': '広島県', 'count': 100}, {'prefecture': '長崎県', 'count': 97}, {'prefecture': '福岡県', 'count': 96}, {'prefecture': '岐阜県', 'count': 95}, {'prefecture': '福島県', 'count': 89}, {'prefecture': '三重県', 'count': 86}, {'prefecture': '山口県', 'count': 86}, {'prefecture': '大分県', 'count': 84}, {'prefecture': '富山県', 'count': 76}, {'prefecture': '愛媛県', 'count': 71}, {'prefecture': '秋田県', 'count': 66}, {'prefecture': '香川県', 'count': 65}, {'prefecture': '長野県', 'count': 65}, {'prefecture': '山形県', 'count': 59}, {'prefecture': '佐賀県', 'count': 57}, {'prefecture': '石川県', 'count': 55}, '...(remaining elements truncated)...']>
        return queryset

class DamIdViewSet(DamViewSet):

    filterset_class = DamIdFilter
    serializer_class = DamIdSerializer #DamGeoFeatureModelSerializer





# class DamCardlistViewSet(viewsets.ModelViewSet):
#     """ CardList用View
#     """
#     queryset = Dam.objects.all()
#     # ここをGEOではなく普通のDRFに変更
#     serializer_class = DamSerializer#DamGeoFeatureModelSerializer#DamSerializer
#     pagination_class = DamCardlistPagination
#     filter_backends = (filters.DjangoFilterBackend,DistanceToPointFilter,) #
#     distance_filter_field = 'geom'
#     distance_filter_convert_meters = True
#     filterset_class = DamFilter


# class DamCardListViewSet(viewsets.ViewSet):
#
#     # 二時間キャッシュ
#     @method_decorator(cache_page(60*60*2))
#     @method_decorator(vary_on_cookie)
#     def list(self, request):
#         queryset = Dam.objects.all()
#         serializer = DamCardSerializer(queryset, many=True)
#
#         # キャッシュがきいているかどうか確認するのにかんたんな方法はプリントされるかどうか。効いている間はされない。
#         #print("Am I Printed?")
#         return Response(serializer.data)


class DamCardListViewSet(viewsets.ModelViewSet):
    # issue_84 で、ページネーションを使うことにした
    queryset = Dam.objects.all()
    serializer_class = DamCardSerializer
    pagination_class = DamPagination



    # ordering_filter = filters.OrderingFilter()
    #
    # def filter_queryset(self, queryset):
    #     queryset = super(DamCardListViewSet, self).filter_queryset(queryset)
    #     return self.ordering_filter.filter_queryset(self.request, queryset, self)


    # filter_backends = [filters.OrderingFilter]
    # ordering_fields = ['total_pondage']




class DamMapListViewSet(viewsets.ViewSet, APIView):
    # permission_classes = (IsAuthenticatedOrReadOnly,)
    permission_classes = (AllowAny,)

    @method_decorator(cache_page(60*60*2))
    @method_decorator(vary_on_cookie)
    def list(self, request):
        queryset = Dam.objects.all()
        serializer = DamMapModelSerializer(queryset, many=True)
        # キャッシュがきいているかどうか確認するのにかんたんな方法はプリントされるかどうか。効いている間はされない。
        #print("Am I Printed?")
        return Response(serializer.data)


