# Generated by Django 3.0.5 on 2020-06-06 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0008_player_coins'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='bounty',
            field=models.IntegerField(default=0),
        ),
    ]