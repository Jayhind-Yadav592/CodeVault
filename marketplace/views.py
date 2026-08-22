from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.db.models import F
from .models import MarketplaceListing, Tag, SavedProject, Watchlist, SearchQueryLog
from .serializers import (
    MarketplaceListingSerializer, TagSerializer,
    SavedProjectSerializer, WatchlistSerializer
)
from .services import SearchService, RecommendationService

class MarketplaceListingViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Public discovery endpoint for marketplace listings.
    Only exposes PUBLISHED and PUBLIC listings.
    """
    serializer_class = MarketplaceListingSerializer
    permission_classes = [AllowAny]
    
    def get_queryset(self):
        query = self.request.query_params.get('q', '')
        
        # Build filters safely
        filters = {}
        for param in ['language', 'category', 'min_loc']:
            if self.request.query_params.get(param):
                filters[param] = self.request.query_params.get(param)
                
        qs = SearchService.search_listings(query=query, filters=filters)
        
        # Log the search asynchronously (or directly here for simplicity)
        if query:
            user = self.request.user if self.request.user.is_authenticated else None
            SearchQueryLog.objects.create(
                user=user,
                query_text=query,
                filters=filters,
                result_count=qs.count()
            )
            
        return qs

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        # Increment views safely using F()
        if instance.visibility == MarketplaceListing.Visibility.PUBLIC:
            MarketplaceListing.objects.filter(pk=instance.pk).update(views_count=F('views_count') + 1)
        return super().retrieve(request, *args, **kwargs)

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def recommendations(self, request):
        qs = RecommendationService.get_recommendations(request.user)
        # Construct explanations mapping
        data = self.get_serializer(qs, many=True).data
        # Mocking explicit explanations for demo purposes, in prod it would map per listing
        for item in data:
            item['recommendation_reason'] = "Matches your saved project categories/languages."
            
        return Response(data)

class SavedProjectViewSet(viewsets.ModelViewSet):
    serializer_class = SavedProjectSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return SavedProject.objects.filter(user=self.request.user).select_related('listing__project')
        
    def perform_create(self, serializer):
        listing = serializer.validated_data['listing']
        # Atomic counter increment
        MarketplaceListing.objects.filter(pk=listing.pk).update(saves_count=F('saves_count') + 1)
        serializer.save(user=self.request.user)

class WatchlistViewSet(viewsets.ModelViewSet):
    serializer_class = WatchlistSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Watchlist.objects.filter(user=self.request.user).select_related('listing__project')
        
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PublicProfileViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]
    
    @action(detail=True, methods=['get'])
    def developer(self, request, pk=None):
        from developers.models import DeveloperProfile
        profile = DeveloperProfile.objects.filter(pk=pk).first()
        if not profile:
            return Response(status=404)
            
        return Response({
            'name': profile.display_name,
            'bio': profile.professional_bio,
            'skills': profile.skills,
            'years_of_experience': profile.years_of_experience,
            'verified': profile.verification_status == 'verified'
        })

    @action(detail=True, methods=['get'])
    def organization(self, request, pk=None):
        from licensing.models import Organization
        org = Organization.objects.filter(pk=pk).first()
        if not org:
            return Response(status=404)
            
        return Response({
            'name': org.name,
            'description': org.description,
            'website': org.website,
            'verified': org.verification_status == 'verified'
        })
