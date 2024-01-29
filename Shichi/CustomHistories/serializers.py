from rest_framework import serializers
from .models import CustomHistories
from CustomAdvertisement.serializers import customAdvertisementCreateSerializer

class CustomHistoriesSerializer(serializers.ModelSerializer):
    advertisement = customAdvertisementCreateSerializer()
    class Meta:
        model = CustomHistories
        fields = '__all__'
class CustomHistoriesSerializerBackDoor(serializers.ModelSerializer):
    class Meta:
        model = CustomHistories
        fields = '__all__'
