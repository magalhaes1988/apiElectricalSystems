# Generated by Django 4.2.7 on 2023-11-19 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_loadgroup_is_discharge_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='electricalcharges',
            name='is_discharge_equipament',
        ),
    ]
