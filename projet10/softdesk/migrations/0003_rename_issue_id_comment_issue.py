# Generated by Django 4.0.3 on 2022-03-31 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('softdesk', '0002_rename_auth_user_id_comment_auth_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='issue_id',
            new_name='issue',
        ),
    ]