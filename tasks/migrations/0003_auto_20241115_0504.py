# Generated by Django 3.0.6 on 2024-11-15 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20241115_0459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_tasks',
            name='priority',
            field=models.CharField(choices=[('P1', 'P1'), ('P2', 'P2'), ('P3', 'P3')], default='P1', max_length=20),
        ),
    ]
