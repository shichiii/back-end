from django.shortcuts import render
from rest_framework import generics
from .models import CustomCarImage
from .serializers import CustomCarImageSerializer

class CustomCarImageListView(generics.ListAPIView):
    queryset = CustomCarImage.objects.all()
    serializer_class = CustomCarImageSerializer
    
class CustomCarImageCreateView(generics.CreateAPIView):
    queryset = CustomCarImage.objects.all()
    serializer_class = CustomCarImageSerializer

class CustomCarImageUpdateView(generics.UpdateAPIView):
    queryset = CustomCarImage.objects.all()
    serializer_class = CustomCarImageSerializer

class CustomCarImageDeleteView(generics.DestroyAPIView):
    queryset = CustomCarImage.objects.all()
    serializer_class = CustomCarImageSerializer
