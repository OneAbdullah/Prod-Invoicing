# Generated by Django 3.2.15 on 2023-07-09 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_apartment_aprt_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='new_tenant_added',
            field=models.BooleanField(default=False),
        ),
    ]
