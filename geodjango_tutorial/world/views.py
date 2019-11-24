from django.shortcuts import render
from rest_framework import viewsets 
from rest_framework_gis.filters import DistanceToPointFilter, InBBoxFilter 

#DistanceToPointFilter: 指定した点からの距離で絞り込むフィルタ
#InBBoxFilter: バウンダリでの絞り込むフィルタ。南西端、北東端の経度、緯度を指定する

from rest_framework.pagination import PageNumberPagination

from .serializers import SchoolSerializer, FacilitySerializer, BusstopSerializer
from .models import School, Facility, Busstop

class MyPagination(PageNumberPagination):
	page_size_param = 'page_size'

class SchoolViewSet(viewsets.ModelViewSet):
	queryset = School.objects.all()
	serializer_class = SchoolSerializer
	pagenation_class = MyPagination

	# データを絞り込む方法を設定
	filter_backends = (DistanceToPointFilter, )
	
	# フィルタの対象フィールドを設定
	distance_filter_field = 'geom'
	
	# 距離でのフィルタ (かも？)
	distance_filter_convert_meters = True 


class FacilityViewSet(viewsets.ModelViewSet):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer
    pagination_class = MyPagination
    filter_backends = (DistanceToPointFilter,)
    distance_filter_field = 'geom'
    distance_filter_convert_meters = False

class BusstopViewSet(viewsets.ModelViewSet):
    queryset = Busstop.objects.all()
    serializer_class = BusstopSerializer
    pagination_class = MyPagination
    filter_backends = (DistanceToPointFilter, InBBoxFilter)
    distance_filter_field = bbox_filter_field = 'geom'
    distance_filter_convert_meters = True