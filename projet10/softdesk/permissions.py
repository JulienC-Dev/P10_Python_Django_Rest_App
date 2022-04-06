from rest_framework import permissions


class ProjectIsAuthenticated(permissions.BasePermission):
    """
    Seuls les contributeurs ou le responsable authentifiés peuvent accéder aux détails et modif du projet.
    Suppression ou modification du projet uniquement par l'auteur
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        if request.method == "GET":
            qs = obj.contributor_set.filter(user__username__contains=request.user.username)
            if not qs:
                return False
            else:
                return True
        if request.method == "PUT" or request.method == "DELETE":
            qs = obj.contributor_set.filter(user__username__contains=request.user.username,
                                            role__contains="responsable")
            if not qs:
                return False
            else:
                return True


class ContributorAuthenticated(permissions.BasePermission):
    """
    Seul l'auteur du projet authentifié peut modifier ou supprimer les utilisateurs du projet
    le GET est accessible à l'auteur du projet et aux contributeurs authentifiés
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        if request.method == "POST":
            responsable_qs = obj.contributor_set.filter(user__username__contains=request.user.username,
                                            role__contains="responsable")
            user_already_add = obj.contributor_set.filter(user__username=request.data.get('user'))
            if not responsable_qs:
                return False
            if user_already_add:
                return False
            return True

        if request.method == "DELETE":
            project = obj.project
            responsable_qs = project.contributor_set.filter(user__username__contains=request.user.username,
                                                        role__contains="responsable")
            user_already_add = project.contributor_set.filter(user__username=request.data.get('user'))
            if not responsable_qs:
                return False
            if user_already_add:
                return False
            return True

# class IssueAuthenticated(permissions.BasePermission):

