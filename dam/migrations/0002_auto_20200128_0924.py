# Generated by Django 2.2 on 2020-01-28 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dam', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='damcarddistributionplace',
            name='dam',
            field=models.ManyToManyField(blank=True, related_name='card_distribution_places', to='dam.Dam'),
        ),
    ]
