from django.urls import path
from .views import CustomAdvertisementFilterView

urlpatterns = [
    path('customadvertisements/filter/', CustomAdvertisementFilterView.as_view(), name='filter'),
]
