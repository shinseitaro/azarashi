from django.shortcuts import render
from rest_framework import generics,viewsets

from rest_framework_gis.filters import DistanceToPointFilter
from rest_framework_gis.pagination import GeoJsonPagination
from rest_framework.pagination import PageNumberPagination
from django_filters import rest_framework as filters 


from dam.models import Dam 
from v1.serializers import DamGeoFeatureModelSerializer

class GeojsonLocationList(generics.ListCreateAPIView):
    pagination_class = GeoJsonPagination

# ページネーションは、settings.py の REST_FRAMEWORK で設定した
# class MyPagination(PageNumberPagination):
# 	page_size_param = 'page_size'
# 

class DamFilter(filters.FilterSet):
    # この変数名が、 url のクエリ文字列キーになる
    # 例: `api/dam/?prefecture=愛知` 
    prefecture = filters.CharFilter(field_name='address', lookup_expr='startswith')
    river = filters.CharFilter(field_name='river_name', lookup_expr='startswith')
    water_system = filters.CharFilter(field_name='water_system_name', lookup_expr='startswith')
    class Meta:
        model = Dam
        fields = ("name", "address", )
        
        


class DamViewSet(viewsets.ModelViewSet):

    queryset = Dam.objects.all()
    serializer_class = DamGeoFeatureModelSerializer
    #pagination_class = MyPagination#GeojsonLocationList
    filter_backends = (filters.DjangoFilterBackend,DistanceToPointFilter,) #
    distance_filter_field = 'geom'
    distance_filter_convert_meters = True
    filterset_class = DamFilter





# Create your views here.
