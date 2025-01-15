# Generated by Django 3.0.6 on 2024-11-14 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_tasks',
            name='priority',
            field=models.CharField(choices=[('Active', 'Active'), ('Closed', 'Closed')], default='P1', max_length=20),
        ),
        migrations.AlterField(
            model_name='user_tasks',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Closed', 'Closed')], default='Active', max_length=20),
        ),
    ]
