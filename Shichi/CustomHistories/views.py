from rest_framework import viewsets
from .models import CustomHistories
from .serializers import CustomHistoriesSerializer

class CustomHistoriesViewSet(viewsets.ModelViewSet):
    queryset = CustomHistories.objects.select_related('advertisement').all()
    serializer_class = CustomHistoriesSerializer
