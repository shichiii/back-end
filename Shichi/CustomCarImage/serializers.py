from rest_framework import serializers
from .models import CustomCarImage

class CustomCarImageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomCarImage
        fields = ['id', 'image', 'index']
        read_only_fields = ['id']
        
class CustomCarImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomCarImage
        fields = ['id', 'image', 'index']