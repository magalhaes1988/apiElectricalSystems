# Generated by Django 4.2.7 on 2023-11-23 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0023_alter_loaddescriptionbycircuit_load_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_id',
            field=models.BigIntegerField(auto_created=True, editable=False),
        ),
    ]