from rest_framework import serializers
from .models import Refresco, Cereales

class RefrescoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Refresco
        fields='__all__'
        
        
class CerealesSerializer(serializers.ModelSerializer):
    class Meta:
        model= Cereales
        fields='__all__'      
