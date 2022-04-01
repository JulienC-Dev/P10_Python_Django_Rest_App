from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import (ProjetsSerializers,
                          ContributorsSerializers,
                          IssueSerializers,
                          CommentSerializers)
from .models import (Project,
                     Contributor,
                     Issue,
                     Comment)
from authentication.models import User


class ProjectsAPI(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ProjetsSerializers

    def get_queryset(self):
        user = self.request.user
        return Project.objects.filter(auth_user_id=user)

    def perform_create(self, serializer):
        serializer.save(auth_user_id=self.request.user)
        project_id = serializer.instance.project_id
        contributor = Contributor(user=self.request.user, project_id=project_id, role='responsable')
        contributor.save()


class ContributorsAPI(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ContributorsSerializers

    def list(self, request, *args, **kwargs):
        project_id = self.kwargs.get('project_id')
        contributor = Contributor.objects.filter(project_id=project_id)
        serializer = self.serializer_class(contributor, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        project_id = self.kwargs.get('project_id')
        user = request.data.get('user')
        try:
            user = User.objects.get(username=user)
        except:
            raise status.HTTP_404_NOT_FOUND
        contributor = Contributor(user=user, project_id=project_id, role='contributeur')
        contributor.save()
        return Response({"success: contributeur ajouté"})

    def get_object(self):
        if self.kwargs['user_id'] is not None:
            obj = Contributor.objects.filter(user_id=self.kwargs['user_id'], project_id=self.kwargs['project_id'])
            return obj


class IssueAPI(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = IssueSerializers

    def perform_create(self, serializer):
        project_id = self.kwargs.get('project_id')
        project = Project.objects.get(project_id=project_id)
        serializer.save(project=project, createur_issue=self.request.user)

    def list(self, request, *args, **kwargs):
        project_id = self.kwargs.get('project_id')
        issue = Issue.objects.filter(project_id=project_id)
        serializer = self.serializer_class(issue, many=True)
        return Response(serializer.data)

    def get_object(self):
        if self.kwargs['issue_id'] is not None:
            obj = Issue.objects.get(id=self.kwargs['issue_id'])
            self.check_object_permissions(self.request, obj)
            return obj
        raise status.HTTP_404_NOT_FOUND


class CommentAPI(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerializers

    def list(self, request, *args, **kwargs):
        issue_id = self.kwargs.get('issue_id')
        comment = Comment.objects.filter(issue_id=issue_id)
        serializer = self.serializer_class(comment, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        issue_id = self.kwargs.get('issue_id')
        issue = Issue.objects.get(id=issue_id)
        serializer.save(issue=issue, auth_user=self.request.user)

    def get_object(self):
        if self.kwargs['comment_id'] is not None:
            obj = Comment.objects.get(comment_id=self.kwargs['comment_id'])
            self.check_object_permissions(self.request, obj)
            return obj
        raise status.HTTP_404_NOT_FOUND
