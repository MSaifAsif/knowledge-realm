from rest_framework_mongoengine import serializers
from .models import Resource


class ResourceSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Resource
        fields = '__all__'
