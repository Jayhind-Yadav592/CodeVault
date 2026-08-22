from rest_framework import serializers
from .models import (
    Organization, LicenseType, LicenseProduct, LicenseRequest, 
    LicenseTerms, NegotiationProposal, Agreement, SignatureRequest
)

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'
        read_only_fields = ('verification_status', 'verified_date', 'owner')

class LicenseTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LicenseType
        fields = '__all__'

class LicenseProductSerializer(serializers.ModelSerializer):
    project_name = serializers.CharField(source='project.name', read_only=True)
    
    class Meta:
        model = LicenseProduct
        fields = '__all__'
        read_only_fields = ('status', 'approved_review_case')

class LicenseTermsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LicenseTerms
        fields = '__all__'
        read_only_fields = ('request', 'version', 'is_accepted')

class NegotiationProposalSerializer(serializers.ModelSerializer):
    terms = LicenseTermsSerializer(read_only=True)
    author_email = serializers.EmailField(source='author.email', read_only=True)
    
    class Meta:
        model = NegotiationProposal
        fields = '__all__'
        read_only_fields = ('request', 'author')

class LicenseRequestSerializer(serializers.ModelSerializer):
    organization_name = serializers.CharField(source='organization.name', read_only=True)
    
    class Meta:
        model = LicenseRequest
        fields = '__all__'
        read_only_fields = ('status',)

class AgreementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agreement
        fields = '__all__'
        read_only_fields = ('request', 'terms', 'version', 'status')

class SignatureRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignatureRequest
        fields = '__all__'
        read_only_fields = ('status', 'signed_at', 'ip_address')
