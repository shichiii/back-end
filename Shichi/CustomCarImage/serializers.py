from rest_framework import serializers
from .models import CustomCarImage

class CustomCarImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomCarImage
        fields = ('image', 'index')