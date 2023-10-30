from rest_framework import serializers
from .models import CustomAdvertisement
from CustomAdvertisementLocation.serializers import CustomAdvertisementLocationSerializers
from CustomCarImage.serializers import CustomCarImageSerializers

class customAdvertisementCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomAdvertisement
        fields = ['id', 'owner_id', 'title', 'start_date', 'end_date', 'price', 'description', 'car_name', 'car_color', 'car_producted_date', 'car_category']
        read_only_fields = ['id', 'owner_id']


class customAdvertisementSerializer(serializers.ModelSerializer):
    location = CustomAdvertisementLocationSerializers(read_only=True)
    car_images = CustomCarImageSerializers(read_only=True)
    class Meta:
        model = CustomAdvertisement
        fields = ['id', 'owner_id', 'location', 'title', 'start_date', 'end_date', 'price', 'description', 'car_images', 'car_name', 'car_color', 'car_producted_date', 'car_category']