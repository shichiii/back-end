from django.urls import path
from .views import customAdvertisementShowView, customAdvertisementViewSet, customAdvertisementCreateView, customAdvertisementDeleteView,customAdvertisementUpdateView,customAdvertisementSearchView, CustomAdvertisementFilterView
from .views import CommentViewSet, CommentCreateView, CommentDeleteView, CommentUpdateView
urlpatterns = [
    path('list/', customAdvertisementViewSet.as_view({'get': 'list'}), name='advertisement_list'),
    path('show/<int:id>/', customAdvertisementShowView.as_view(), name='advertisement_show'),
    path('create/', customAdvertisementCreateView.as_view(), name='advertisement_create'),
    path('delete/<int:pk>/', customAdvertisementDeleteView.as_view(), name='advertisement_delete'),
    path('update/<int:pk>/', customAdvertisementUpdateView.as_view(), name='advertisement_update'),
    path('search/', customAdvertisementSearchView.as_view(), name='advertisement_search'),
    path('filter/', CustomAdvertisementFilterView.as_view(), name='advertisement_filter'),
    
    path('list-comment/', CommentViewSet.as_view({'get': 'list'}), name = 'list-comment'),
    path('create-comment/', CommentCreateView.as_view(), name='create-comment'),
    path('delete-comment/<int:pk>/', CommentDeleteView.as_view(), name='delete-comment'),
    path('update-comment/<int:pk>/', CommentUpdateView.as_view(), name='update-comment'),
]
