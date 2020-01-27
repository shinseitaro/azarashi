from rest_framework import viewsets
from rest_framework_gis.filters import DistanceToPointFilter, InBBoxFilter
from rest_framework.pagination import PageNumberPagination

from .serializers import DamSerializer
from .models import Dam

class MyPagination(PageNumberPagination):
    page_size_param = 'page_size'

class DamViewSet(viewsets.ModelViewSet):
    queryset = Dam.objects.all()
    serializer_class = DamSerializer
    pagination_class = MyPagination

    filter_backends = (DistanceToPointFilter, )
    distance_filter_field = 'geom'
    distance_filter_convert_meters = True

