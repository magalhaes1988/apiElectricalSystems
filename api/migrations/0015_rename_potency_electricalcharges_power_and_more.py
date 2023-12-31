# Generated by Django 4.2.7 on 2023-11-19 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_remove_electricalcharges_is_discharge_equipament'),
    ]

    operations = [
        migrations.RenameField(
            model_name='electricalcharges',
            old_name='potency',
            new_name='power',
        ),
        migrations.RenameField(
            model_name='electricalcharges',
            old_name='potency_factor',
            new_name='power_factor',
        ),
        migrations.AddField(
            model_name='electricalcharges',
            name='reactive_power',
            field=models.PositiveBigIntegerField(blank=True, editable=False, null=True),
        ),
    ]
