# Generated by Django 2.2 on 2020-01-25 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0002_card_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='file_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
