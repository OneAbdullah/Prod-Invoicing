# Generated by Django 3.2.15 on 2023-05-11 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20230510_2345'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_profile',
            old_name='delete_report_allowed',
            new_name='delete_invoice_allowed',
        ),
    ]
