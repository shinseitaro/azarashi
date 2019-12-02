from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from dam.models import Dam, Institution, Purpose


class DamSerializer(serializers.ModelSerializer):

	class Meta:
		model = Dam
		exclude = ["registered_at", "modified_at"]


class DamListSerializer(serializers.ListSerializer):
	"""複数ダムを扱う
	"""
	child = DamSerializer()

class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields = ('name',)

class PurposeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purpose
        fields = ('name',)


class DamGeoFeatureModelSerializer(GeoFeatureModelSerializer):
    type_code = serializers.CharField(source='type_code.description')
    institution_in_charge = InstitutionSerializer(read_only=True, many=True)
    purpose_code = PurposeSerializer(read_only=True, many=True)

    class Meta:
        model = Dam
        geo_field = "geom"
        id_field = False
        exclude = ("registered_at", "modified_at", "id")
    # fields = ("name", "address", "river_name")
