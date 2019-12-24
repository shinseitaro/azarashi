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


from dam.models import Dam
from v1.serializers import DamGeoFeatureModelSerializer, DamSerializer, DamListSerializer, DamCardListSerializer,DamCardSerializer, DamMapModelSerializer

class GeojsonLocationList(generics.ListCreateAPIView):
    pagination_class = GeoJsonPagination

class DamPagination(PageNumberPagination):
    # url のリクエスト　例：GET /api/dam/?page=2
    page_size_query_param = 'page_size'
    # 一ページあたりの件数
    page_size = 100

class DamFilter(filters.FilterSet):
    # この変数名が、 url のクエリ文字列キーになる
    # 例: `api/dam/?prefecture=愛知`
    prefecture = filters.CharFilter(field_name='address', lookup_expr='contains')
    river = filters.CharFilter(field_name='river_name', lookup_expr='contains')
    water_system = filters.CharFilter(field_name='water_system_name', lookup_expr='contains')
    class Meta:
        model = Dam
        fields = ("name", "address", )

class DamViewSet(viewsets.ModelViewSet):

    queryset = Dam.objects.all()
    serializer_class = DamGeoFeatureModelSerializer
    pagination_class = DamPagination
    filter_backends = (filters.DjangoFilterBackend,DistanceToPointFilter,) #
    distance_filter_field = 'geom'
    distance_filter_convert_meters = True
    filterset_class = DamFilter
    http_method_names = ['get', 'head', 'option']

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

class DamCardListViewSet(viewsets.ViewSet):
    # ＃　キャッシュのためにModelViewSetは使えないので、コメントアウト
    # queryset = Dam.objects.all()
    # serializer_class = DamCardSerializer

    # 二時間キャッシュ
    @method_decorator(cache_page(60*60*2))
    @method_decorator(vary_on_cookie)
    def list(self, request):
        queryset = Dam.objects.all()
        serializer = DamCardSerializer(queryset, many=True)
        # キャッシュがきいているかどうか確認するのにかんたんな方法はプリントされるかどうか。効いている間はされない。
        #print("Am I Printed?")
        return Response(serializer.data)


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




