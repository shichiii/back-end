from django.urls import path
from .views import customAdvertisementSearchView, CustomAdvertisementFilterView

urlpatterns = [
    path('customadvertisements/search/', customAdvertisementSearchView.as_view(), name='search'),
    path('customadvertisements/filter/', CustomAdvertisementFilterView.as_view(), name='filter'),
]
