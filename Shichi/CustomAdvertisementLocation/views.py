from django.shortcuts import render
from rest_framework import generics
from .models import CustomAdvertisementLocation
from .serializers import CustomAdvertisementLocationSerializer

class customAdvertisementLocationShowView(generics.RetrieveAPIView):
    queryset = CustomAdvertisementLocation.objects.all()
    serializer_class = CustomAdvertisementLocationSerializer
    lookup_field = 'id'

class CustomAdvertisementLocationListView(generics.ListAPIView):
    queryset = CustomAdvertisementLocation.objects.all()
    serializer_class = CustomAdvertisementLocationSerializer

class CustomAdvertisementLocationCreateView(generics.CreateAPIView):
    queryset = CustomAdvertisementLocation.objects.all()
    serializer_class = CustomAdvertisementLocationSerializer

class CustomAdvertisementLocationUpdateView(generics.UpdateAPIView):
    queryset = CustomAdvertisementLocation.objects.all()
    serializer_class = CustomAdvertisementLocationSerializer

class CustomAdvertisementLocationDeleteView(generics.DestroyAPIView):
    queryset = CustomAdvertisementLocation.objects.all()
    serializer_class = CustomAdvertisementLocationSerializer