from django.shortcuts import render

# Create your views here.
from .serializer import RefrescoSerializer, CerealesSerializer
from .models import Refresco, Cereales
from rest_framework import viewsets

class RefrescoViewset(viewsets.ModelViewSet):
    queryset=Refresco.objects.all()
    serializer_class=RefrescoSerializer
    
class CerealesViewset(viewsets.ModelViewSet):
    queryset=Cereales.objects.all()
    serializer_class=CerealesSerializer