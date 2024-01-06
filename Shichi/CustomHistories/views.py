from rest_framework.views import APIView
from rest_framework import viewsets
from .models import CustomHistories
from CustomAdvertisement.models import CustomAdvertisement
from .serializers import CustomHistoriesSerializer , CustomHistoriesSerializerBackDoor
from rest_framework.response import Response
from rest_framework import status

class CustomHistoriesViewSetBackdoor(viewsets.ModelViewSet):
    queryset = CustomHistories.objects.select_related('advertisement').all()
    serializer_class = CustomHistoriesSerializerBackDoor
    
class CustomHistoriesViewSet(APIView):
    queryset = CustomHistories.objects.select_related('advertisement').all()
    serializer_class = CustomHistoriesSerializer

    def get(self, request):
        queryset = CustomHistories.objects.filter(user=request.user.id)
        if queryset.exists():
            all_serializers = CustomHistoriesSerializer(queryset, many=True)
            return Response(all_serializers.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response([], status=status.HTTP_404_NOT_FOUND)