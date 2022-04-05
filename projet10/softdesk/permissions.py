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


# class ContributorAuthenticated(permissions.BasePermission):
#     """
#     Seuls les contributeurs ou le responsable authentifiés du projet peuvent ajouter des users ou les deletes.
#     """
#     def has_permission(self, request, view):
#         return bool(request.user and request.user.is_authenticated)
#
#     def has_object_permission(self, request, view, obj):
#         if request.method == "POST":
#             user_already_add = obj.contributor_set.filter(user__username=request.data.get('user'))
#             request_user_already_add = obj.contributor_set.filter(user__username=request.user)
#             if user_already_add:
#                 return False
#             if not request_user_already_add:
#                 return False
#             else:
#                 return True
#
#         if request.method == "DELETE":
#             project = obj.project
#             user_already_add = project.contributor_set.filter(user__username=request.data.get('user'))
#             request_user_already_add = project.contributor_set.filter(user__username=request.user)
#             if user_already_add:
#                 return False
#             if not request_user_already_add:
#                 return False
#             else:
#                 return True

