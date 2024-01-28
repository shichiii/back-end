from django.urls import path
from .views import CustomDateListView, CustomDateCreateView, CustomDateUpdateView, CustomDateDeleteView, CustomDateShowView

urlpatterns = [
    path('show/<int:id>/', CustomDateShowView.as_view(), name='show'),
    path('list/', CustomDateListView.as_view(), name='list'),
    path('create/', CustomDateCreateView.as_view(), name='create'),
    path('<int:pk>/update/', CustomDateUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', CustomDateDeleteView.as_view(), name='delete'),
]