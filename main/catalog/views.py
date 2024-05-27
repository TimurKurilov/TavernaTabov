from django.shortcuts import render
from rest_framework import viewsets
from .models import ElectroGuitar
from .serializers import ElectroGuitarSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class ElectroGuitarViewsets(viewsets.ModelViewSet):
    queryset = ElectroGuitar.objects.all()
    serializer_class = ElectroGuitarSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filterset_fields = ('color', 'brand', 'form', 'rate')
    search_fields = ('color', 'brand', 'form')
    ordering_fields = ('color', 'brand', 'form', 'rate')
    ordering = ('brand')
    