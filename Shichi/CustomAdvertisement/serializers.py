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
    #car_images = CustomCarImageSerializer(read_only=True, many=True)
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
    
from CustomUser.models import CustomUser

class user_profile_image(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['profile_image']
class CommentSerializer(serializers.ModelSerializer):
    user_first_name = serializers.SerializerMethodField()
    user_last_name = serializers.SerializerMethodField()
    user_profile_image = serializers.SerializerMethodField()
    class Meta:
        model = Comment
        fields = ['id', 'adv', 'user_id', 'user_profile_image','user_first_name', 'user_last_name', 'created_date', 'text']
        read_only_fields = ['user_profile_image','user_first_name', 'user_last_name', 'created_date']

    def get_user_first_name(self, obj):
        try:
            user = CustomUser.objects.get(id=obj.user_id)
            return user.first_name
        except CustomUser.DoesNotExist:
            return None

    def get_user_last_name(self, obj):
        try:
            user = CustomUser.objects.get(id=obj.user_id)
            return user.last_name
        except CustomUser.DoesNotExist:
            return None
        
    def get_user_profile_image(self, obj):
        try:
            user = CustomUser.objects.get(id=obj.user_id)
            # print(type(user.profile_image.url))
            # breakpoint()
            if not user.profile_image:
                return None  
            else:
                return user.profile_image.url
            
        except CustomUser.DoesNotExist:
            return None  
        
class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = '__all__'
        