# Generated by Django 4.2.7 on 2023-11-24 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0026_alter_loaddescriptionbycircuit_electrical_charge_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loaddescription',
            name='electrical_charges',
            field=models.ManyToManyField(through='api.LoadDescriptionByCircuit', to='api.electricalcharges'),
        ),
    ]
