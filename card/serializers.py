from rest_framework import serializers
from .models import Card


class CardSerializer(serializers.ModelSerializer):
    user = serializers.CurrentUserDefault()

    class Meta:
        model = Card
        fields = '__all__'
