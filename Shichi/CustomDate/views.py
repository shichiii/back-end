from django.shortcuts import render
from rest_framework import generics
from .models import CustomDate
from .serializers import CustomDateSerializer, CustomDateCreateSerializer

class CustomDateShowView(generics.RetrieveAPIView):
    queryset = CustomDate.objects.all()
    serializer_class = CustomDateSerializer
    lookup_field = 'id'

class CustomDateListView(generics.ListAPIView):
    queryset = CustomDate.objects.all()
    serializer_class = CustomDateSerializer
    
class CustomDateCreateView(generics.CreateAPIView):
    queryset = CustomDate.objects.all()
    serializer_class = CustomDateCreateSerializer

class CustomDateUpdateView(generics.UpdateAPIView):
    queryset = CustomDate.objects.all()
    serializer_class = CustomDateSerializer

class CustomDateDeleteView(generics.DestroyAPIView):
    queryset = CustomDate.objects.all()
    serializer_class = CustomDateSerializer
