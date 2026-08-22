from rest_framework import serializers
from .models import (
    ReviewCase, ReviewerAssignment, ReviewChecklistItem, 
    ReviewComment, RemediationItem, ReviewTransitionHistory
)

class ReviewTransitionHistorySerializer(serializers.ModelSerializer):
    actor_email = serializers.EmailField(source='actor.email', read_only=True)
    
    class Meta:
        model = ReviewTransitionHistory
        fields = ('id', 'actor_email', 'previous_state', 'new_state', 'reason', 'created_at')

class ReviewerAssignmentSerializer(serializers.ModelSerializer):
    user_email = serializers.EmailField(source='user.email', read_only=True)
    
    class Meta:
        model = ReviewerAssignment
        fields = ('id', 'user', 'user_email', 'role')

class ReviewChecklistItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewChecklistItem
        fields = '__all__'

class ReviewCommentSerializer(serializers.ModelSerializer):
    author_email = serializers.EmailField(source='author.email', read_only=True)
    
    class Meta:
        model = ReviewComment
        fields = '__all__'
        read_only_fields = ('author',)

class RemediationItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = RemediationItem
        fields = '__all__'

class ReviewCaseSerializer(serializers.ModelSerializer):
    assignments = ReviewerAssignmentSerializer(many=True, read_only=True)
    
    class Meta:
        model = ReviewCase
        fields = (
            'id', 'project', 'snapshot', 'compliance_evaluation',
            'state', 'priority', 'due_date', 'previous_case',
            'assignments', 'created_at', 'updated_at'
        )
        read_only_fields = ('state',)
