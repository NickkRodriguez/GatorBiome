from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Wine
from .serializers import WineSerializer

class WineViewSet(viewsets.ModelViewSet):
    queryset = Wine.objects.all()
    serializer_class = WineSerializer
