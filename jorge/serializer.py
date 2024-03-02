from rest_framework import serializers
from .models import Refresco

class RefrescoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Refresco
        fields='__all__'
        
        
