from rest_framework import serializers
from .models import (Project,
                     Contributor,
                     Issue,
                     Comment)
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
    issue_id = serializers.IntegerField(source='id', required=False)
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
    created_time = serializers.DateTimeField(
        format="%Y-%m-%d %H:%M:%S",
        required=False)

    class Meta:
        model = Issue
        fields = ['issue_id',
                  'project_id',
                  'createur_issue',
                  'assignee',
                  'title',
                  'description',
                  'created_time',
                  'priority',
                  'status',
                  'balise']

    def create(self, validated_data):
        if validated_data.get("assignee") is None:
            validated_data['assignee'] = validated_data.get("createur_issue")
        return Issue.objects.create(**validated_data)


class CommentSerializers(serializers.ModelSerializer):
    auth_user = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )
    created_time = serializers.DateTimeField(
        format="%Y-%m-%d %H:%M:%S",
        required=False)
    class Meta:
        model = Comment
        fields = ['comment_id',
                  'issue_id',
                  'auth_user',
                  'description',
                  'created_time'
                  ]