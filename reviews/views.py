from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import (
    ReviewCase, ReviewChecklistItem, ReviewComment, RemediationItem
)
from .serializers import (
    ReviewCaseSerializer, ReviewChecklistItemSerializer,
    ReviewCommentSerializer, RemediationItemSerializer, ReviewTransitionHistorySerializer
)
from .services import ReviewService

class ReviewCaseViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewCaseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Admins/Reviewers see all. Developers see their own.
        if self.request.user.is_staff:
            return ReviewCase.objects.all()
        return ReviewCase.objects.filter(project__owner=self.request.user)

    @action(detail=True, methods=['post'])
    def transition(self, request, pk=None):
        case = self.get_object()
        target_state = request.data.get('target_state')
        reason = request.data.get('reason', '')
        
        try:
            updated_case = ReviewService.transition_case(case, target_state, request.user, reason)
            return Response(self.get_serializer(updated_case).data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def generate_checklist(self, request, pk=None):
        case = self.get_object()
        ReviewService.generate_checklist(case)
        items = case.checklist_items.all()
        return Response(ReviewChecklistItemSerializer(items, many=True).data)
        
    @action(detail=True, methods=['get'])
    def timeline(self, request, pk=None):
        case = self.get_object()
        history = case.transitions.all().order_by('created_at')
        return Response(ReviewTransitionHistorySerializer(history, many=True).data)

class ReviewChecklistItemViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewChecklistItemSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        if self.request.user.is_staff:
            return ReviewChecklistItem.objects.all()
        return ReviewChecklistItem.objects.filter(case__project__owner=self.request.user)

class ReviewCommentViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewCommentSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        qs = ReviewComment.objects.all()
        if not self.request.user.is_staff:
            # Developers cannot see internal notes
            qs = qs.filter(case__project__owner=self.request.user, is_internal=False)
        return qs

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class RemediationItemViewSet(viewsets.ModelViewSet):
    serializer_class = RemediationItemSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        if self.request.user.is_staff:
            return RemediationItem.objects.all()
        return RemediationItem.objects.filter(case__project__owner=self.request.user)
