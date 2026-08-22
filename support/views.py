from rest_framework import viewsets, permissions
from rest_framework.serializers import ModelSerializer
from .models import Ticket, TicketComment

class TicketSerializer(ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'

class TicketCommentSerializer(ModelSerializer):
    class Meta:
        model = TicketComment
        fields = '__all__'

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [permissions.IsAuthenticated]

class TicketCommentViewSet(viewsets.ModelViewSet):
    queryset = TicketComment.objects.all()
    serializer_class = TicketCommentSerializer
    permission_classes = [permissions.IsAuthenticated]