from rest_framework import viewsets, permissions
from rest_framework.serializers import ModelSerializer
from .models import Incident, IncidentEvent, Postmortem

class IncidentSerializer(ModelSerializer):
    class Meta:
        model = Incident
        fields = '__all__'

class IncidentEventSerializer(ModelSerializer):
    class Meta:
        model = IncidentEvent
        fields = '__all__'

class PostmortemSerializer(ModelSerializer):
    class Meta:
        model = Postmortem
        fields = '__all__'

class IncidentViewSet(viewsets.ModelViewSet):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer
    permission_classes = [permissions.IsAuthenticated]

class IncidentEventViewSet(viewsets.ModelViewSet):
    queryset = IncidentEvent.objects.all()
    serializer_class = IncidentEventSerializer
    permission_classes = [permissions.IsAuthenticated]

class PostmortemViewSet(viewsets.ModelViewSet):
    queryset = Postmortem.objects.all()
    serializer_class = PostmortemSerializer
    permission_classes = [permissions.IsAuthenticated]