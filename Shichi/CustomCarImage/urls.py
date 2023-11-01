from django.urls import path
from .views import CustomCarImageListView, CustomCarImageCreateView, CustomCarImageUpdateView, CustomCarImageDeleteView

urlpatterns = [
    path('customcarimages/list/', CustomCarImageListView.as_view(), name='list'),
    path('customcarimages/create/', CustomCarImageCreateView.as_view(), name='create'),
    path('customcarimages/<int:pk>/update/', CustomCarImageUpdateView.as_view(), name='update'),
    path('customcarimages/<int:pk>/delete/', CustomCarImageDeleteView.as_view(), name='delete'),
]