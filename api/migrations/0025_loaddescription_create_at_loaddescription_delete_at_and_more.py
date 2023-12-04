# Generated by Django 4.2.7 on 2023-11-23 14:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0024_alter_project_project_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='loaddescription',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loaddescription',
            name='delete_at',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='loaddescription',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='loaddescription',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
