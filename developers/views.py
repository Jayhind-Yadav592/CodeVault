from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import DeveloperProfile
from .serializers import DeveloperProfileSerializer

class DeveloperProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = DeveloperProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        # Create profile if it doesn't exist
        profile, created = DeveloperProfile.objects.get_or_create(user=self.request.user)
        return profile

class DashboardStatsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        projects = user.owned_projects.all()
        
        # We handle deleted objects in Manager (SoftDeleteManager)
        stats = {
            'total_projects': projects.count(),
            'draft_projects': projects.filter(state='draft').count(),
            'submitted_projects': projects.filter(state='submitted').count(),
            'under_review': projects.filter(state__in=['under_review', 'technical_review', 'compliance_review']).count(),
            'approved_projects': projects.filter(state='approved').count(),
            'rejected_projects': projects.filter(state='rejected').count(),
        }
        
        if hasattr(user, 'developer_profile'):
            stats['profile_completion'] = user.developer_profile.completion_percentage
        else:
            stats['profile_completion'] = 0

        return Response(stats)
