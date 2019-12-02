from rest_framework import serializers 
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from dam.models import Dam 

class DamSerializer(serializers.ModelSerializer):

	class Meta: 
		model = Dam 
		exclude = ["registered_at", "modified_at"]


class DamListSerializer(serializers.ListSerializer):
	"""複数ダムを扱う
	"""
	child = DamSerializer()

class DamGeoFeatureModelSerializer(GeoFeatureModelSerializer):

	class Meta: 
		model = Dam 
		geo_field = "geom"
		id_field = False
		exclude = ("registered_at", "modified_at", "id" )
		#fields = ("name", "address", "river_name")