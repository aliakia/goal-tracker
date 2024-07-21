from rest_framework import viewsets
from .serializers import JournalSerializer
from ..models import Journal

class JournalViewSet(viewsets.ModelViewSet):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
