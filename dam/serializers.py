from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from .models import Dam

class DamSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Dam
        fields = '__all__'

