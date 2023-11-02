from rest_framework import serializers
from .models import CustomAdvertisementLocation

class CustomAdvertisementLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomAdvertisementLocation
        fields = '__all__'