from rest_framework import viewsets, response
from .models import Resource
from .serializers import ResourceSerializer


class ResourceViewSet(viewsets.ModelViewSet):
    queryset = Resource.objects.all()
    lookup_field = 'id'
    serializer_class = ResourceSerializer
