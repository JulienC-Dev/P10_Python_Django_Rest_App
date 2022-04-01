# Generated by Django 4.0.3 on 2022-03-31 14:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('project_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('back-end', 'back-end'), ('front-end', 'front-end'), ('iOS ou Android', 'iOS ou Android')], default='back-end', max_length=100)),
                ('auth_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('priority', models.CharField(choices=[('faible', 'faible'), ('moyenne', 'moyenne'), ('elevee', 'élevée')], default='faible', max_length=100)),
                ('status', models.CharField(choices=[('afaire', 'À faire'), ('encours', 'En cours'), ('termine', 'Terminé')], default='afaire', max_length=100)),
                ('balise', models.CharField(choices=[('bug', 'bug'), ('amelioration', 'amélioration'), ('tache', 'tâche')], default='bug', max_length=100)),
                ('assignee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignee', to=settings.AUTH_USER_MODEL)),
                ('createur_issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='createur', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='softdesk.project')),
            ],
        ),
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('contributeur', 'contributeur'), ('responsable', 'responsable')], default='contributeur', max_length=100)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='softdesk.project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=200)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('auth_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('issue_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='softdesk.issue')),
            ],
        ),
    ]
