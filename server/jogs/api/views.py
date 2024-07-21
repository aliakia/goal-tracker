from rest_framework import viewsets
from .serializers import JogsSerializer
from ..models import Jogs

class JogsViewSet(viewsets.ModelViewSet):
    queryset = Jogs.objects.all()
    serializer_class = JogsSerializer