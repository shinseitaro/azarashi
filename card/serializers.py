from rest_framework import serializers
from .models import Card
from user.models import User
from dam.models import Dam


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name')


class DamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dam
        fields = ('dam_code', 'name', 'address', 'water_system_name', 'river_name')


class CardSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True, default=serializers.CurrentUserDefault())
    dam = DamSerializer(read_only=True)

    class Meta:
        model = Card
        fields = '__all__'
