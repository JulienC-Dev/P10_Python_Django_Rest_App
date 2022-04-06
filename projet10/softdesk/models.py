from django.db import models
from django.conf import settings

from django.utils.translation import gettext_lazy as _


class Project(models.Model):
    TYPE_BACK_END = (
        ('back-end', _('back-end')),
        ('front-end', _('front-end')),
        ('iOS', _('iOS')),
        ('Android', _('Android')),
    )
    project_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    type = models.CharField(choices=TYPE_BACK_END, max_length=100, default='back-end')
    auth_user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Contributor(models.Model):
    TYPE_ROLE = (
        ('contributeur', _('contributeur')),
        ('responsable', _('responsable')),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    role = models.CharField(choices=TYPE_ROLE, max_length=100, default='contributeur')

    def __str__(self):
        return '{}'.format(self.user)



class Issue(models.Model):
    TYPE_PRIORITY = (
        ('faible', _('faible')),
        ('moyenne', _('moyenne')),
        ('elevee', _('élevée')),
    )

    TYPE_STATUS = (
        ('afaire', _('À faire')),
        ('encours', _('En cours')),
        ('termine', _('Terminé')),
    )

    TYPE_BALISE = (
        ('bug', _('bug')),
        ('amelioration', _('amélioration')),
        ('tache', _('tâche')),
    )
    createur_issue = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='createur')
    assignee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='assignee')
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    created_time = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(choices=TYPE_PRIORITY, max_length=100, default='faible')
    status = models.CharField(choices=TYPE_STATUS, max_length=100, default='afaire')
    balise = models.CharField(choices=TYPE_BALISE, max_length=100, default='bug')


class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    auth_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    created_time = models.DateTimeField(auto_now_add=True)