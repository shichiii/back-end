from rest_framework import serializers
from .models import CustomDate

class CustomDateCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomDate
        fields = ['id', 'date', 'adv_id']
        read_only_fields = ['id']
        
class CustomDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomDate
        fields = ['id', 'date', 'adv_id']