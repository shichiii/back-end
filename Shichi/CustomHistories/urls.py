from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomHistoriesViewSet

router = DefaultRouter()
router.register(r'customhistories', CustomHistoriesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]