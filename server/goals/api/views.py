from rest_framework import viewsets
from .serializers import PersonSerializers
from ..models import Person

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializers