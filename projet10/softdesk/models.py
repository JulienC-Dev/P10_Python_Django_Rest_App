from django.db import models
from django.conf import settings

from django.utils.translation import gettext_lazy as _


TYPE_BACK_END = (
    ('back-end', _('back-end')),
    ('front-end', _('front-end')),
    ('iOS ou Android', _('iOS ou Android')),
)

TYPE_ROLE = (
    ('contributeur', _('contributeur')),
    ('responsable', _('responsable')),
)


class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    type = models.CharField(choices=TYPE_BACK_END, max_length=100, default='back-end')
    auth_user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Contributor(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    role = models.CharField(choices=TYPE_ROLE, max_length=100, default='contributeur')


class Issue(models.Model):
    createur_issue = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='createur')
    assignee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='assignee')
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
