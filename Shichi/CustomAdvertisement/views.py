from django.shortcuts import render
from rest_framework import generics, viewsets, filters
from .models import CustomAdvertisement, Comment, Rate
from .serializers import customAdvertisementCreateSerializer, customAdvertisementSerializer, CommentSerializer, RateSerializer
from rest_framework import generics, viewsets, filters, status
from rest_framework.response import Response
from CustomUser.models import CustomUser

class customAdvertisementShowView(generics.RetrieveAPIView):
    queryset = CustomAdvertisement.objects.all()
    serializer_class = customAdvertisementSerializer
    lookup_field = 'id'

class customAdvertisementViewSet(viewsets.ModelViewSet):
    queryset = CustomAdvertisement.objects.all()
    serializer_class = customAdvertisementSerializer

class customAdvertisementCreateView(generics.CreateAPIView):
    queryset = CustomAdvertisement.objects.all()
    serializer_class = customAdvertisementCreateSerializer
    
    def perform_create(self, serializer):
        user = self.request.user
        user = CustomUser.objects.get(id=user.id)
        if user is None:
            return Response({'error': 'User does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        serializer.save(owner_id=user.pk)

class customAdvertisementDeleteView(generics.DestroyAPIView):
    queryset = CustomAdvertisement.objects.all()
    serializer_class = customAdvertisementSerializer

class customAdvertisementUpdateView(generics.UpdateAPIView):
    queryset = CustomAdvertisement.objects.all()
    serializer_class = customAdvertisementCreateSerializer

    
class customAdvertisementSearchView(generics.ListAPIView):
    queryset = CustomAdvertisement.objects.all()
    serializer_class = customAdvertisementSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['car_name', 'car_category', 'title']
    
class CustomAdvertisementFilterView(generics.ListAPIView):
    queryset = CustomAdvertisement.objects.all()
    serializer_class = customAdvertisementSerializer
    filter_backends = [filters.OrderingFilter]

    def get_queryset(self):
        queryset = super().get_queryset()
        
        lower_price_input = self.request.query_params.get('lower_price', 0)
        upper_price_input = self.request.query_params.get('upper_price', 99999999999999999)
        car_category_input = self.request.query_params.get('car_category', None)
        car_color_input = self.request.query_params.get('car_color', None)
        
        if car_category_input:
            queryset = queryset.filter(car_category__icontains=car_category_input)

        if car_color_input:
            queryset = queryset.filter(car_color__icontains=car_color_input)

        queryset = queryset.filter(price__range=(lower_price_input, upper_price_input))
        return queryset
    
    
    
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentCreateView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentDeleteView(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentUpdateView(generics.UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class RateViewSet(viewsets.ModelViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer
class RateCreateView(generics.CreateAPIView):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer

class RateDeleteView(generics.DestroyAPIView):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer

class RateUpdateView(generics.UpdateAPIView):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer

