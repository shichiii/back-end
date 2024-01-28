from django.urls import path
from .views import CustomDateListView, CustomDateCreateView, CustomDateUpdateView, CustomDateDeleteView, CustomDateShowView

urlpatterns = [
    path('show/<int:id>/', CustomDateShowView.as_view(), name='date-show'),
    path('list/', CustomDateListView.as_view(), name='date-list'),
    path('create/', CustomDateCreateView.as_view(), name='date-create'),
    path('<int:pk>/update/', CustomDateUpdateView.as_view(), name='date-update'),
    path('<int:pk>/delete/', CustomDateDeleteView.as_view(), name='date-delete'),
]