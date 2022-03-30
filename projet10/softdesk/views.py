from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import (ProjetsSerializers,
                          ContributorsSerializers,
                          IssueSerializers)
from .models import (Project,
                     Contributor,
                     Issue)
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