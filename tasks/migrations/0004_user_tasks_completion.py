# Generated by Django 3.0.6 on 2024-11-15 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_auto_20241115_0504'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_tasks',
            name='completion',
            field=models.DateField(blank=True, null=True),
        ),
    ]