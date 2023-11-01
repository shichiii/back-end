from rest_framework import serializers
from .models import CustomAdvertisement, Comment
from CustomAdvertisementLocation.serializers import CustomAdvertisementLocationSerializer
from CustomCarImage.serializers import CustomCarImageSerializer

class customAdvertisementCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomAdvertisement
        fields = ['id', 'owner_id', 'title', 'start_date', 'end_date', 'price', 'description', 'car_name', 'car_color', 'car_producted_date', 'car_category']
        read_only_fields = ['id', 'owner_id']


class customAdvertisementSerializer(serializers.ModelSerializer):
    location = CustomAdvertisementLocationSerializer(read_only=True)
    car_images = CustomCarImageSerializer(read_only=True)
    class Meta:
        model = CustomAdvertisement
        fields = ['id', 'owner_id', 'location', 'title', 'start_date', 'end_date', 'price', 'description', 'car_images', 'car_name', 'car_color', 'car_producted_date', 'car_category']
        
# class UserCommentSerializer(serializers.ModelSerializer):	
#     class Meta:	
#         model = User	
#         fields = ['username']

# class CommentSerializer(serializers.ModelSerializer):
#     # user = UserCommentSerializer(read_only=True)
#     class Meta:
#         model = Comment
#         fields = ['id', 'created_date', 'text', 'adv']
#         read_only_fields = ['id', 'created_date', 'adv']

#     def create(self, validated_data):
#         request = self.context.get("request")
#         validated_data['place_id'] = self.context.get("adv")
#         validated_data['user'] = request.user
#         return super().create(validated_data)

#     def update(self, instance, validated_data):
#         validated_data['created_date'] = datetime.now()
#         return super().update(instance, validated_data)