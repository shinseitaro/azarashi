# Generated by Django 2.1.11 on 2020-01-15 00:28

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('infrastructure', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dam',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='名称')),
                ('address', models.CharField(max_length=60, verbose_name='住所')),
                ('registered_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified_at', models.DateTimeField(blank=True, null=True)),
                ('url', models.URLField(blank=True)),
                ('dam_code', models.IntegerField()),
                ('water_system_name', models.CharField(blank=True, max_length=50, null=True)),
                ('river_name', models.CharField(blank=True, max_length=50, null=True)),
                ('scale_bank_height', models.FloatField(blank=True, null=True)),
                ('scale_bank_span', models.FloatField(blank=True, null=True)),
                ('bank_volume', models.IntegerField(blank=True, null=True)),
                ('total_pondage', models.IntegerField(blank=True, null=True)),
                ('year_of_completion', models.CharField(blank=True, max_length=10, null=True)),
                ('positional_information_precision', models.IntegerField(blank=True, null=True)),
                ('geom', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4019)),
                ('prefecture', models.CharField(blank=True, max_length=4, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='infrastructure.Category', verbose_name='カテゴリ')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DamCardDistributionPlace',
            fields=[
                ('id', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('url', models.URLField()),
                ('address', models.CharField(max_length=100)),
                ('operation_hour', models.CharField(max_length=200)),
                ('prefecture', models.CharField(max_length=4)),
                ('mon', models.BooleanField(default=False)),
                ('tue', models.BooleanField(default=False)),
                ('wed', models.BooleanField(default=False)),
                ('thu', models.BooleanField(default=False)),
                ('fri', models.BooleanField(default=False)),
                ('sat', models.BooleanField(default=False)),
                ('sun', models.BooleanField(default=False)),
                ('dam', models.ManyToManyField(blank=True, to='dam.Dam')),
            ],
        ),
        migrations.CreateModel(
            name='DamType',
            fields=[
                ('id', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Purpose',
            fields=[
                ('id', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='dam',
            name='institution_in_charge',
            field=models.ManyToManyField(blank=True, to='dam.Institution'),
        ),
        migrations.AddField(
            model_name='dam',
            name='purpose_code',
            field=models.ManyToManyField(blank=True, to='dam.Purpose'),
        ),
        migrations.AddField(
            model_name='dam',
            name='type_code',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dam.DamType'),
        ),
    ]