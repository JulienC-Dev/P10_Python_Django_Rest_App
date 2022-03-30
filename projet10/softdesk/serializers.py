from rest_framework import serializers
from .models import (Project,
                     Contributor,
                     Issue)
from authentication.models import User


class ContributorsSerializers(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username'
    )

    class Meta:
        model = Contributor
        fields = ['user']


class ProjetsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['project_id', 'title', 'description', 'type']


class IssueSerializers(serializers.ModelSerializer):
    project_id = serializers.PrimaryKeyRelatedField(read_only=True, source='project.project_id')
    assignee = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username',
        allow_null=True,
        required=False
    )
    createur_issue = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        model = Issue
        fields = ['project_id', 'createur_issue', 'assignee', 'title', 'description']

    def create(self, validated_data):
        if validated_data.get("assignee") is None:
            validated_data['assignee'] = validated_data.get("createur_issue")
        return Issue.objects.create(**validated_data)
