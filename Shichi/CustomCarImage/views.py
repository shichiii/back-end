from django.shortcuts import render
from rest_framework import generics , parsers
from .models import CustomCarImage
from .serializers import CustomCarImageSerializer
from drf_yasg.utils import swagger_auto_schema

class CustomCarImageShowView(generics.RetrieveAPIView):
    queryset = CustomCarImage.objects.all()
    serializer_class = CustomCarImageSerializer
    lookup_field = 'id'

class CustomCarImageListView(generics.ListAPIView):
    queryset = CustomCarImage.objects.all()
    serializer_class = CustomCarImageSerializer
    
class CustomCarImageCreateView(generics.CreateAPIView):
    parser_classes = (parsers.MultiPartParser,)
    queryset = CustomCarImage.objects.all()
    serializer_class = CustomCarImageSerializer
    @swagger_auto_schema(request_body=CustomCarImageSerializer ,operation_description='Upload file...',)
    def post(self, request, *args, **kwargs):
        """
        Upload a custom car image.
        """
        return super().post(request, *args, **kwargs)

class CustomCarImageUpdateView(generics.UpdateAPIView):
    queryset = CustomCarImage.objects.all()
    serializer_class = CustomCarImageSerializer

class CustomCarImageDeleteView(generics.DestroyAPIView):
    queryset = CustomCarImage.objects.all()
    serializer_class = CustomCarImageSerializer
