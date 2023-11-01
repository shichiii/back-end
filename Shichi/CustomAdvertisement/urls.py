from django.urls import path
from .views import customAdvertisementShowView, customAdvertisementViewSet, customAdvertisementCreateView, customAdvertisementDeleteView,customAdvertisementUpdateView,customAdvertisementSearchView, CustomAdvertisementFilterView

urlpatterns = [
    path('customadvertisements/list/', customAdvertisementViewSet.as_view({'get': 'list'}), name='list'),
    path('customadvertisements/<int:id>/show', customAdvertisementShowView.as_view(), name='show'),
    path('customadvertisements/<int:id>/create/', customAdvertisementCreateView.as_view(), name='create'),
    path('customadvertisements/<int:id>/delete/', customAdvertisementDeleteView.as_view(), name='delete'),
    path('customadvertisements/<int:id>/update/', customAdvertisementUpdateView.as_view(), name='update'),
    path('customadvertisements/search/', customAdvertisementSearchView.as_view(), name='search'),
    path('customadvertisements/filter/', CustomAdvertisementFilterView.as_view(), name='filter'),
]
