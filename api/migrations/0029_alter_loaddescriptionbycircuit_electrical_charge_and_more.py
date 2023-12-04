# Generated by Django 4.2.7 on 2023-11-24 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0028_alter_loaddescription_electrical_charges'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loaddescriptionbycircuit',
            name='electrical_charge',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ecc', to='api.electricalcharges'),
        ),
        migrations.AlterField(
            model_name='loaddescriptionbycircuit',
            name='load_description',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ldc', to='api.loaddescription'),
        ),
    ]
