from django.contrib import admin

from authentication.models import User
from softdesk.models import (Project,
                             Contributor,
                             Issue,
                             Comment)


class ProjetAdmin(admin.ModelAdmin):
    list_display = ('project_id', 'title', 'description', 'type', 'auth_user_id')


class ContributorAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'user', 'project_id', 'role')


class IssueAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_id', 'createur_issue', 'assignee', 'title', 'description')


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment_id', 'get_project', 'issue_id', 'description', 'auth_user', 'created_time')

    @admin.display( description='Project ID')
    def get_project(self, obj):
        return obj.issue.project_id


admin.site.register(User, UserAdmin)
admin.site.register(Project, ProjetAdmin)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Issue, IssueAdmin)
admin.site.register(Comment, CommentAdmin)