# Generated by Django 5.2.3 on 2025-06-27 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workflows', '0006_installedplugin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='installedplugin',
            name='user_config',
        ),
    ]
