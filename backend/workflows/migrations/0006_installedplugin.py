# Generated by Django 5.2.3 on 2025-06-26 07:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflows', '0005_delete_installedplugin'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='InstalledPlugin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=200)),
                ('version', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('author', models.CharField(max_length=200)),
                ('icon', models.TextField()),
                ('config_schema', models.JSONField()),
                ('user_config', models.JSONField()),
                ('installed_at', models.DateTimeField(auto_now_add=True)),
                ('installed_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('workspace', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='installed_plugins', to='workflows.workspace')),
            ],
            options={
                'unique_together': {('workspace', 'slug')},
            },
        ),
    ]
