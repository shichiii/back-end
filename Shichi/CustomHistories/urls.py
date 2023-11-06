from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomHistoriesViewSet , CustomHistoriesViewSetBackdoor

router = DefaultRouter()
router.register(r'backdoor', CustomHistoriesViewSetBackdoor)

urlpatterns = [
    path('', include(router.urls)),
    path('customhistories', CustomHistoriesViewSet.as_view()),
]