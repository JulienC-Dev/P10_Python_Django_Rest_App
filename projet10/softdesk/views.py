from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from .permissions import (ProjectIsAuthenticated,
                          ContributorAuthenticated,
                          IssueAuthenticated,
                          CommentAuthenticated)
from .serializers import (ProjetsSerializers,
                          ContributorsSerializers,
                          IssueSerializers,
                          CommentSerializers)
from .models import (Project,
                     Contributor,
                     Issue,
                     Comment)
from authentication.models import User
from django.shortcuts import get_object_or_404


class ProjectsAPI(viewsets.ModelViewSet):
    permission_classes = [ProjectIsAuthenticated]
    serializer_class = ProjetsSerializers

    def get_queryset(self):
        """
        Renvoie uniquement les projets rattachés à l'utilisateur connecté
        """
        user = self.request.user
        qs_project = Project.objects.filter(auth_user_id=user)
        qs_contributor = Contributor.objects.filter(user=user)
        project_id_contributor = [x.project_id for x in qs_contributor]
        qs_contributor = Project.objects.filter(project_id__in=project_id_contributor)
        qs = qs_project.union(qs_contributor)
        return qs

    def list(self, request, *args, **kwargs):
        qs = self.get_queryset()
        if not qs:
            return Response(status=status.HTTP_403_FORBIDDEN)
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(auth_user_id=self.request.user)
        project_id = serializer.instance.project_id
        contributor = Contributor(user=self.request.user, project_id=project_id, role='responsable')
        contributor.save()

    def get_object(self):
        obj = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        self.check_object_permissions(self.request, obj)
        return obj


class ContributorsAPI(viewsets.ModelViewSet):
    permission_classes = [ContributorAuthenticated]
    serializer_class = ContributorsSerializers

    def get_queryset(self):
        """
        Renvoie pour un projet la liste des collaborateurs et du responsable
        Seul les collaborateurs et responsable ont accès à la liste
        """
        project_id = self.kwargs.get('project_id')
        project = Project.objects.get(project_id=project_id)
        qs = project.contributor_set.filter(user__username=self.request.user.username)
        """
        Renvoie un query vide si le self.request.user n'est pas un contributeur du projet
        """
        if not qs:
            return qs
        qs = project.contributor_set.all()
        return qs

    def list(self, request, *args, **kwargs):
        qs = self.get_queryset()
        if not qs:
            return Response(status=status.HTTP_403_FORBIDDEN)
        serializer = self.serializer_class(qs, many=True)
        response = Response(serializer.data)
        return response

    def create(self, request, *args, **kwargs):
        project_id = self.kwargs.get('project_id')
        user = request.data.get('user')
        try:
            user = User.objects.get(username=user)
            project = Project.objects.get(project_id=project_id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        contributor = Contributor(user=user, project=project, role='contributeur')
        self.check_object_permissions(self.request, project)
        serializer = self.get_serializer(contributor)
        contributor.save()
        return Response(serializer.data)

    def get_object(self):
        if self.kwargs['user_id'] is not None:
            obj = Contributor.objects.filter(user_id=self.kwargs['user_id'], project_id=self.kwargs['project_id'])
            return obj

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if not instance:
            return Response(status=status.HTTP_404_NOT_FOUND)
        self.check_object_permissions(self.request, instance.get())
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class IssueAPI(viewsets.ModelViewSet):
    permission_classes = [IssueAuthenticated]
    serializer_class = IssueSerializers

    def get_queryset(self):
        qs = Issue.objects.filter(createur_issue=self.request.user, project=self.kwargs['project_id'])
        return qs

    def list(self, request, *args, **kwargs):
        qs = self.get_queryset()
        serializer = self.serializer_class(qs, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        project_id = self.kwargs.get('project_id')
        project = Project.objects.get(project_id=project_id)
        self.check_object_permissions(self.request, project)
        serializer.save(project=project, createur_issue=self.request.user)

    def get_object(self):
        if self.kwargs['issue_id'] is not None:
            obj = Issue.objects.get(id=self.kwargs['issue_id'])
            self.check_object_permissions(self.request, obj)
            return obj
        raise status.HTTP_404_NOT_FOUND


class CommentAPI(viewsets.ModelViewSet):
    permission_classes = [CommentAuthenticated]
    serializer_class = CommentSerializers

    def get_queryset(self):
        """
        Renvoie une liste de commentaires si le self.request.user est un contributeur du projet
        """
        qs_contributor = Contributor.objects.filter(project__project_id=self.kwargs.get('project_id'),
                                                    role="contributeur", user=self.request.user)
        if not qs_contributor:
            return qs_contributor
        comment = Comment.objects.filter(issue_id=self.kwargs.get('issue_id'))
        return comment

    def list(self, request, *args, **kwargs):
        comment = self.get_queryset()
        serializer = self.serializer_class(comment, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        issue_id = self.kwargs.get('issue_id')
        issue = Issue.objects.get(id=issue_id)
        projet = Project.objects.get(project_id=self.kwargs['project_id'])
        self.check_object_permissions(self.request, projet)
        serializer.save(issue=issue, auth_user=self.request.user)

    def get_object(self):
        if self.kwargs['comment_id'] is not None:
            obj = Comment.objects.get(comment_id=self.kwargs['comment_id'])
            self.check_object_permissions(self.request, obj)
            return obj
        raise status.HTTP_404_NOT_FOUND
