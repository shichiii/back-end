from django.urls import path
from .views import CustomCarImageListView, CustomCarImageCreateView, CustomCarImageUpdateView, CustomCarImageDeleteView, CustomCarImageShowView

urlpatterns = [
    path('show/<int:id>/', CustomCarImageShowView.as_view(), name='show'),
    path('list/', CustomCarImageListView.as_view(), name='list'),
    path('create/', CustomCarImageCreateView.as_view(), name='create'),
    path('<int:pk>/update/', CustomCarImageUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', CustomCarImageDeleteView.as_view(), name='delete'),
]