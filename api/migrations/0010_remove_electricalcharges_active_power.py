# Generated by Django 4.2.7 on 2023-11-19 04:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_electricalcharges'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='electricalcharges',
            name='active_power',
        ),
    ]
