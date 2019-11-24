from rest_framework import serializers 
from .models import Dam

class DamSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Dam
        fields = ('__all__')

