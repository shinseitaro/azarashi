from rest_framework import serializers
from .models import Card


class CardSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Card
        fields = '__all__'
