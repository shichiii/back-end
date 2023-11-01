from django.urls import path
from .views import customAdvertisementShowView, customAdvertisementViewSet, customAdvertisementCreateView, customAdvertisementDeleteView,customAdvertisementUpdateView,customAdvertisementSearchView, CustomAdvertisementFilterView, CommentViewSet

urlpatterns = [
    path('list/', customAdvertisementViewSet.as_view({'get': 'list'}), name='advertisement_list'),
    path('show/<int:id>/', customAdvertisementShowView.as_view(), name='advertisement_show'),
    path('create/', customAdvertisementCreateView.as_view(), name='advertisement_create'),
    path('delete/<int:id>/', customAdvertisementDeleteView.as_view(), name='advertisement_delete'),
    path('update/<int:id>/', customAdvertisementUpdateView.as_view(), name='advertisement_update'),
    path('search/', customAdvertisementSearchView.as_view(), name='advertisement_search'),
    path('filter/', CustomAdvertisementFilterView.as_view(), name='advertisement_filter'),
    
    path('adv/<int:pk>/add-comment/', CommentViewSet.as_view(), name = 'add_comment'),
]
