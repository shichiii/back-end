from django.urls import path
from .views import CustomAdvertisementLocationCreateView, CustomAdvertisementLocationUpdateView, CustomAdvertisementLocationDeleteView, customAdvertisementLocationShowView, CustomAdvertisementLocationListView

urlpatterns = [
    path('show/<int:id>/', customAdvertisementLocationShowView.as_view(), name='show'),
    path('list/', CustomAdvertisementLocationListView.as_view(), name='list'),
    path('create/', CustomAdvertisementLocationCreateView.as_view(), name='create'),
    path('<int:pk>/update/', CustomAdvertisementLocationUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', CustomAdvertisementLocationDeleteView.as_view(), name='delete'),
]