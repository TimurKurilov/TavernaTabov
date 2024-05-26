from rest_framework import serializers
from .models import ElectroGuitar

class ElectroGuitarSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectroGuitar
        fields = ('color', 'brand', 'form')
    