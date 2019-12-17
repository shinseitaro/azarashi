from rest_framework import serializers
from .models import Card


class CardSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Card
        fields = ('user', 'comment', 'published_date')
