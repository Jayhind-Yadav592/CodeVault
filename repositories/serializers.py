from rest_framework import serializers
from .models import RepositoryConnection, AnalysisJob, AnalysisSnapshot, LanguageStat, ClassificationStat, PullRequestStat

class LanguageStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = LanguageStat
        fields = ('language_name', 'file_count', 'loc')

class ClassificationStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassificationStat
        fields = ('category', 'file_count')

class PullRequestStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = PullRequestStat
        fields = ('is_available', 'total_prs', 'open_prs', 'merged_prs')

class AnalysisSnapshotSerializer(serializers.ModelSerializer):
    languages = LanguageStatSerializer(many=True, read_only=True)
    classifications = ClassificationStatSerializer(many=True, read_only=True)
    pr_stats = PullRequestStatSerializer(read_only=True)

    class Meta:
        model = AnalysisSnapshot
        fields = (
            'id', 'commit_hash', 'branch', 'total_files', 'total_loc',
            'meaningful_loc', 'blank_lines', 'comment_lines',
            'total_commits', 'meaningful_commits', 'total_authors',
            'first_commit_date', 'latest_commit_date', 'created_at',
            'languages', 'classifications', 'pr_stats'
        )

class AnalysisJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnalysisJob
        fields = ('id', 'state', 'started_at', 'completed_at', 'error_log', 'created_at')

class RepositoryConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepositoryConnection
        fields = ('id', 'project', 'provider', 'repo_url', 'repo_name', 'default_branch', 'status', 'last_sync_time', 'last_error')
        read_only_fields = ('id', 'status', 'last_sync_time', 'last_error')
