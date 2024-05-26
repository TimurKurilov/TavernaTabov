from django.shortcuts import render
from rest_framework import viewsets
from .models import ElectroGuitar
from .serializers import ElectroGuitarSerializer

class ElectroGuitarViewsets(viewsets.ModelViewSet):
    queryset = ElectroGuitar.objects.all()
    serializer_class = ElectroGuitarSerializer
    
