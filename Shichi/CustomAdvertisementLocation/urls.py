from django.urls import path
from .views import CustomAdvertisementLocationCreateView, CustomAdvertisementLocationUpdateView, CustomAdvertisementLocationDeleteView

urlpatterns = [
    path('customadvertisementlocations/create/', CustomAdvertisementLocationCreateView.as_view(), name='create'),
    path('customadvertisementlocations/<int:pk>/update/', CustomAdvertisementLocationUpdateView.as_view(), name='update'),
    path('customadvertisementlocations/<int:pk>/delete/', CustomAdvertisementLocationDeleteView.as_view(), name='delete'),
]