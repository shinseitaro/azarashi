from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from dam.models import Dam, Institution, Purpose


class DamSerializer(serializers.ModelSerializer):
    class Meta:
        model=Dam
        exclude = ["registered_at", "modified_at"]
        #fields = ("name", "address", "river_name","geom")

class DamCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dam
        exclude = ["registered_at", "modified_at"]
        #fields = ("name", "address","geom")

    def to_representation(self, instance):
        response_dict = super().to_representation(instance)
        response_dict['coordinates'] = instance.geom.coords #['coordinates']
        del response_dict['geom']
        return response_dict


class DamListSerializer(serializers.ListSerializer):
	"""複数ダムを扱う
	"""
	child = DamSerializer()

class DamCardListSerializer(serializers.ListSerializer):
	"""複数ダムカードを扱う
	"""
	child = DamCardSerializer()


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
        #exclude = ("registered_at", "modified_at", )
        fields = ("name", "address", "river_name", "type_code", "institution_in_charge", "purpose_code" )
        #fields = ("name", "address", "river_name",)


class DamMapModelSerializer(GeoFeatureModelSerializer):
    """Dam map 表示のためのシリアライザ。 geom と name だけ。
    """
    class Meta:
        model = Dam
        geo_field = "geom"
        id_field = False
        fields = ("name", "geom",)
