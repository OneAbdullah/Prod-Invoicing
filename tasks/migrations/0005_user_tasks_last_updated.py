# Generated by Django 3.0.6 on 2024-11-16 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_user_tasks_completion'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_tasks',
            name='last_updated',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
