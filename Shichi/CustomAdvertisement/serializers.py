from rest_framework import serializers
from .models import CustomAdvertisement, Comment, Rate
from CustomCarImage.serializers import CustomCarImageSerializer
from CustomDate.models import CustomDate
from django.db.models import Avg
from datetime import timedelta

class customAdvertisementCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomAdvertisement
        fields = ['id', 'owner_id', 'start_date', 'end_date', 'available_date_list', 'price', 'description', 'car_image1', 'car_image2', 'car_image3', 'car_name', 'car_color', 'car_produced_date','car_seat_count','car_door_count', 'car_Is_cooler', 'car_gearbox', 'car_fuel', 'car_category', 'location_state', 'location_geo_width', 'location_geo_length']
        read_only_fields = ['id', 'owner_id', 'available_date_list']  

class customAdvertisementSerializer(serializers.ModelSerializer):
    car_images = CustomCarImageSerializer(read_only=True, many=True)
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = CustomAdvertisement
        fields = ['id', 'average_rating', 'owner_id', 'start_date', 'end_date','available_date_list', 'price', 'description', 'car_image1', 'car_image2', 'car_image3', 'car_name', 'car_color', 'car_produced_date', 'car_seat_count','car_door_count', 'car_Is_cooler', 'car_gearbox', 'car_fuel', 'car_category', 'location_state', 'location_geo_width', 'location_geo_length']
    
    def get_average_rating(self , obj):
        print(obj.id)
        print("*********************************************")
        rates = Rate.objects.filter(adv__id = obj.id).all()
        if rates.exists():
            avg_rating = rates.aggregate(avg_rating = Avg('rate'))['avg_rating']
            return avg_rating
        return 0
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        
class RateSerializer(serializers.ModelSerializer):
    # mean_rate = serializersl
    class Meta:
        model = Rate
        fields = '__all__'
        