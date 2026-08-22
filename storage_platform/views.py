from rest_framework import viewsets, permissions
from rest_framework.serializers import ModelSerializer
from .models import StorageObject

class StorageObjectSerializer(ModelSerializer):
    class Meta:
        model = StorageObject
        fields = '__all__'

class StorageObjectViewSet(viewsets.ModelViewSet):
    queryset = StorageObject.objects.all()
    serializer_class = StorageObjectSerializer
    permission_classes = [permissions.IsAuthenticated]