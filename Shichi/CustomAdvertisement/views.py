from django.shortcuts import render
from rest_framework import generics, viewsets, filters, views
from .models import CustomAdvertisement, Comment, Rate
from .serializers import customAdvertisementCreateSerializer, customAdvertisementSerializer, CommentSerializer, RateSerializer
from rest_framework import generics, viewsets, filters, status
from rest_framework.response import Response
from CustomUser.models import CustomUser
from CustomDate.models import CustomDate
from datetime import datetime, timedelta
from django.db.models import Q

class customAdvertisementShowView(generics.RetrieveAPIView):
    queryset = CustomAdvertisement.objects.all()
    serializer_class = customAdvertisementSerializer
    lookup_field = 'id'

class customAdvertisementViewSet(viewsets.ModelViewSet):
    queryset = CustomAdvertisement.objects.all()
    serializer_class = customAdvertisementSerializer

class customAdvertisementDeleteView(generics.DestroyAPIView):
    queryset = CustomAdvertisement.objects.all()
    serializer_class = customAdvertisementSerializer

class customAdvertisementUpdateView(generics.UpdateAPIView):
    queryset = CustomAdvertisement.objects.all()
    serializer_class = customAdvertisementCreateSerializer

class customAdvertisementCreateView(generics.CreateAPIView):
    queryset = CustomAdvertisement.objects.all()
    serializer_class = customAdvertisementCreateSerializer
    
    def perform_create(self, serializer):       
        user = self.request.user       
        serializer.save(owner_id=user.pk)
        
        id = serializer.data['id']
        start_date = serializer.data['start_date']
        end_date = serializer.data['end_date']
        start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
        end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
        
        available_date_list=[]
        date_range = [start_date + timedelta(days=x) for x in range((end_date - start_date).days + 1)]
        for date in date_range:
            custom_date = CustomDate.objects.create(date=date, adv_id=id)
            available_date_list.append(custom_date)

        instance = CustomAdvertisement.objects.get(id=id)
        instance.available_date_list.set(available_date_list)
        instance.save()
    
class customAdvertisementSearchView(generics.ListAPIView):
    queryset = CustomAdvertisement.objects.all()
    serializer_class = customAdvertisementSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['car_name']
    
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
        start_date_input = self.request.query_params.get('start_date', None)
        end_date_input = self.request.query_params.get('end_date', None)
        state_input = self.request.query_params.get('state', None)
        
        
        if start_date_input and not end_date_input:
            start_date = datetime.strptime(start_date_input, "%Y-%m-%d").date()
            end_date = start_date + timedelta(days=30)
        elif not start_date_input and end_date_input:
            start_date = datetime.now().date()
            end_date = datetime.strptime(end_date_input, "%Y-%m-%d").date()
        elif start_date_input and end_date_input:
            start_date = datetime.strptime(start_date_input, "%Y-%m-%d").date()
            end_date = datetime.strptime(end_date_input, "%Y-%m-%d").date()
            
        if start_date_input or end_date_input:
            queryset = queryset.filter(
                Q(start_date__range=(start_date, end_date)) |
                Q(end_date__range=(start_date, end_date)) |
                Q(available_date_list__date__gte=start_date, available_date_list__date__lte=end_date)
            )
        
        
        if car_category_input:
            queryset = queryset.filter(car_category__icontains=car_category_input)

        if car_color_input:
            queryset = queryset.filter(car_color__icontains=car_color_input)
            
        if state_input:
            queryset = queryset.filter(location_state__icontains=state_input)

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


class PayForAdvertisement(views.APIView):
    def get(self, request, id):
        advertisement = CustomAdvertisement.objects.get(id=id)
        if advertisement is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        email = request.user
        user = CustomUser.objects.get(email=email)
        user_wealth = user.wallet
        cost = advertisement.price
        
        start_date_input = self.request.query_params.get('start_date', None)
        end_date_input = self.request.query_params.get('end_date', None)
        
        start_date = datetime.strptime(start_date_input, "%Y-%m-%d").date()
        end_date = datetime.strptime(end_date_input, "%Y-%m-%d").date()
        date_range = [start_date + timedelta(days=x) for x in range((end_date - start_date).days + 1)]
        
        cost = cost * len(date_range)     
        if user_wealth < cost:
            return Response("Not enough money", status=status.HTTP_406_NOT_ACCEPTABLE)
        else:           
            for date in date_range:
                custom_date = CustomDate.objects.get(date=date, adv_id=id)
                if custom_date is None:
                    return Response(f"The car is not available on {date}", status=status.HTTP_403_FORBIDDEN)
            
            for date in date_range:
                custom_date = CustomDate.objects.get(date=date, adv_id=id)
                advertisement.available_date_list.remove(custom_date)
                custom_date.delete()
            advertisement.save()
            
            user.wallet -= cost
            owner = CustomUser.objects.get(id = advertisement.owner_id)
            owner.wallet += cost
            user.save()
            owner.save()
            
            return Response("Successfull", status=status.HTTP_200_OK)