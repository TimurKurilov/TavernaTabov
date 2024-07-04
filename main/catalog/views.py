from django.shortcuts import render
from rest_framework import viewsets
from .models import ElectroGuitar
from .serializers import ElectroGuitarSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.shortcuts import redirect

def redirectview(request):
    return redirect('http://127.0.0.1:8000/api/')

class ElectroGuitarViewsets(viewsets.ModelViewSet):
    """Список всех электрогитар"""
    
    
    queryset = ElectroGuitar.objects.all()
    serializer_class = ElectroGuitarSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filterset_fields = ('color', 'brand', 'form', 'rate')
    search_fields = ('color', 'brand', 'form')
    ordering_fields = ('color', 'brand', 'form', 'rate')
    ordering = ('brand')
