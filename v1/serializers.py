from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from dam.models import Dam, Institution, Purpose, DamCardDistributionPlace


class DamSerializer(serializers.ModelSerializer):
    class Meta:
        model=Dam
        exclude = ["registered_at", "modified_at"]

class DamStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Dam
        fields = ('id', 'name', 'water_system_name', 'total_pondage')

class DamCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dam
        exclude = ["registered_at", "modified_at"]

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
        fields = ("dam_code", "name", "address", "water_system_name", "river_name", "type_code", "institution_in_charge", "year_of_completion", "purpose_code")


class DamMapModelSerializer(GeoFeatureModelSerializer):
    """Dam map 表示のためのシリアライザ。 geom と name だけ。
    """
    class Meta:
        model = Dam
        geo_field = "geom"
        id_field = False
        fields = ("name", "total_pondage", "year_of_completion", "geom",)


class DamIdSerializer(DamGeoFeatureModelSerializer):

    class Meta:
        model = Dam
        geo_field = "geom"
        #exclude = ["registered_at", "modified_at"]
        # id_field = True
        fields = ("name", "address", "river_name", "type_code", "institution_in_charge", "year_of_completion", "purpose_code", "scale_bank_height", "scale_bank_span", "total_pondage", )


class DamCountSerializer(serializers.Serializer):
    class Meta:
        fields = ("prefecture", "count",)

    def to_representation(self, instance):
        return instance

class DamCardDistributionPlaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = DamCardDistributionPlace
        fields = "__all__"
