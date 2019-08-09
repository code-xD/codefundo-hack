from rest_framework import viewsets
from .models import VoterDetail
from .permissions import IsAdminOrLoggedIn
from .serializer import DetailSerializer
from rest_framework.authentication import BasicAuthentication
# Create your views here.


class VoterViewSet(viewsets.ModelViewSet):
    queryset = VoterDetail.objects.all()
    serializer_class = DetailSerializer
    permission_classes = [IsAdminOrLoggedIn]
    authentication_classes = [BasicAuthentication]
