from django.core.exceptions import ValidationError
from projects.models import Project, OwnershipDeclaration
from security.models import Finding
from .models import MarketplaceListing

class PublicationService:
    @staticmethod
    def validate_for_publication(listing: MarketplaceListing) -> bool:
        """
        Validates if a project can be published.
        Raises ValidationError if rules are violated.
        """
        project = listing.project
        
        # 1. Project must be APPROVED
        if project.state != Project.State.APPROVED:
            raise ValidationError("Project must be in APPROVED state to be published.")
            
        # 2. Must have a signed ownership declaration
        has_declaration = OwnershipDeclaration.objects.filter(
            project=project, status=OwnershipDeclaration.Status.SIGNED
        ).exists()
        if not has_declaration:
            raise ValidationError("Project is missing a signed Ownership Declaration.")
            
        # 3. No blocking critical security findings
        critical_findings = Finding.objects.filter(
            project=project,
            severity=Finding.Severity.CRITICAL,
            status__in=[Finding.Status.OPEN, Finding.Status.ACKNOWLEDGED]
        ).exists()
        if critical_findings:
            raise ValidationError("Project has unresolved CRITICAL security findings.")
            
        # 4. Must have an associated ReviewCase that is APPROVED
        if not listing.review_case or listing.review_case.state != 'approved':
            raise ValidationError("Project must have an approved Review Case.")
            
        return True

    @staticmethod
    def publish(listing: MarketplaceListing, user):
        """
        Attempts to publish a listing.
        """
        if listing.status == MarketplaceListing.Status.PUBLISHED:
            return listing
            
        PublicationService.validate_for_publication(listing)
        
        listing.status = MarketplaceListing.Status.PUBLISHED
        # Make public if it was private by default? Or respect existing visibility choice.
        if listing.visibility == MarketplaceListing.Visibility.PRIVATE:
            listing.visibility = MarketplaceListing.Visibility.PUBLIC
            
        listing.save()
        return listing

class SearchService:
    @staticmethod
    def search_listings(query: str = '', filters: dict = None):
        from django.db.models import Q
        
        # Only search PUBLIC and PUBLISHED listings
        qs = MarketplaceListing.objects.filter(
            visibility=MarketplaceListing.Visibility.PUBLIC,
            status=MarketplaceListing.Status.PUBLISHED
        ).select_related('project', 'project__category').prefetch_related('tags')
        
        if query:
            qs = qs.filter(
                Q(project__name__icontains=query) |
                Q(project__short_description__icontains=query) |
                Q(project__full_description__icontains=query) |
                Q(project__primary_language__icontains=query) |
                Q(tags__name__icontains=query)
            ).distinct()
            
        if filters:
            if 'language' in filters:
                qs = qs.filter(project__primary_language__iexact=filters['language'])
            if 'category' in filters:
                qs = qs.filter(project__category__slug=filters['category'])
            if 'min_loc' in filters:
                qs = qs.filter(project__approximate_loc__gte=filters['min_loc'])
                
        return qs.order_by('-popularity_score', '-created_at')

class RecommendationService:
    @staticmethod
    def get_recommendations(user):
        from .models import SavedProject
        
        # 1. Gather user preferences based on Saved Projects
        saved = SavedProject.objects.filter(user=user).select_related('listing__project')
        
        languages = [s.listing.project.primary_language for s in saved]
        categories = [s.listing.project.category_id for s in saved if s.listing.project.category_id]
        
        if not saved:
            # Fallback to general popularity
            return MarketplaceListing.objects.filter(
                visibility=MarketplaceListing.Visibility.PUBLIC,
                status=MarketplaceListing.Status.PUBLISHED
            ).order_by('-popularity_score')[:5]
            
        # 2. Find similar projects (matching language or category), excluding already saved
        saved_listing_ids = [s.listing_id for s in saved]
        
        from django.db.models import Q
        recommendations = MarketplaceListing.objects.filter(
            visibility=MarketplaceListing.Visibility.PUBLIC,
            status=MarketplaceListing.Status.PUBLISHED
        ).exclude(id__in=saved_listing_ids).filter(
            Q(project__primary_language__in=languages) |
            Q(project__category_id__in=categories)
        ).distinct().order_by('-popularity_score')[:5]
        
        # In a real implementation, we would construct the exact explanation string
        # for why it was recommended, but for ORM retrieval we'll return the queryset.
        return recommendations
