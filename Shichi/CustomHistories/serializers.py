from rest_framework import serializers
from .models import CustomHistories

class CustomHistoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomHistories
        fields = '__all__'
