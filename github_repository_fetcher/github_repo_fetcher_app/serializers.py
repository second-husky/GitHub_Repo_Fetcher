from rest_framework import serializers
from .models import GitHubRepo

class GitHubRepoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GitHubRepo
        fields = ('id', 'username', 'repository')
