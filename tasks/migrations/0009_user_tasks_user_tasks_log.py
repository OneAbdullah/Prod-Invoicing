# Generated by Django 3.0.6 on 2024-11-16 00:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0008_auto_20241116_0544'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_tasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Closed', 'Closed')], default='Active', max_length=20)),
                ('desc', models.TextField(blank=True, max_length=1000, null=True)),
                ('priority', models.CharField(choices=[('P1', 'P1'), ('P2', 'P2'), ('P3', 'P3')], default='P1', max_length=20)),
                ('deadline', models.DateField(blank=True, null=True)),
                ('completion', models.DateField(blank=True, null=True)),
                ('last_updated_at', models.DateTimeField(auto_now_add=True)),
                ('assigned', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assigned_to', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assigned_from', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='user_tasks_log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_updated_at', models.DateTimeField(auto_now_add=True)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.user_tasks')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
