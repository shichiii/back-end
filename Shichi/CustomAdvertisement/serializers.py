from rest_framework import serializers
from .models import CustomAdvertisement, Comment
from CustomAdvertisementLocation.serializers import CustomAdvertisementLocationSerializer
from CustomCarImage.serializers import CustomCarImageSerializer

class customAdvertisementCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomAdvertisement
        fields = ['id', 'owner_id', 'location', 'title', 'start_date', 'end_date', 'price', 'description', 'car_images', 'car_name', 'car_color', 'car_producted_date', 'car_category']
        read_only_fields = ['id']


class customAdvertisementSerializer(serializers.ModelSerializer):
    location = CustomAdvertisementLocationSerializer(read_only=True)
    car_images = CustomCarImageSerializer(read_only=True, many=True)

    class Meta:
        model = CustomAdvertisement
        fields = ['id', 'owner_id', 'location', 'title', 'start_date', 'end_date', 'price', 'description', 'car_images', 'car_name', 'car_color', 'car_producted_date', 'car_category']
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'