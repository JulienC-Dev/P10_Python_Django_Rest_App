from django.contrib import admin

from authentication.models import User
from softdesk.models import (Project,
                             Contributor,
                             Issue)

class ProjetAdmin(admin.ModelAdmin):
    list_display = ('project_id', 'title', 'description', 'type', 'auth_user_id')

class ContributorAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'user', 'project', 'role')

class IssueAdmin(admin.ModelAdmin):
    list_display = ('project_id', 'createur_issue', 'assignee')


admin.site.register(User)
admin.site.register(Project, ProjetAdmin)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Issue, IssueAdmin)