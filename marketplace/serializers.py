from rest_framework import serializers
from .models import MarketplaceListing, Tag, SavedProject, Watchlist
from projects.serializers import ProjectSerializer

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'slug']

class MarketplaceListingSerializer(serializers.ModelSerializer):
    project = ProjectSerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    
    class Meta:
        model = MarketplaceListing
        fields = [
            'id', 'project', 'visibility', 'status', 'tags',
            'popularity_score', 'views_count', 'saves_count', 'is_featured'
        ]

class SavedProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedProject
        fields = ['id', 'listing', 'notes', 'folder', 'created_at']

class WatchlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Watchlist
        fields = ['id', 'listing', 'notify_on_update', 'notify_on_license_change', 'created_at']
