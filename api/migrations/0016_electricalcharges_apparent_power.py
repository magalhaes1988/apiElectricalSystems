# Generated by Django 4.2.7 on 2023-11-19 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_rename_potency_electricalcharges_power_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='electricalcharges',
            name='apparent_power',
            field=models.PositiveBigIntegerField(blank=True, editable=False, null=True),
        ),
    ]
