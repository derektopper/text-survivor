# Generated by Django 3.0.5 on 2020-06-11 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0011_auto_20200611_0103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='receiver',
            field=models.CharField(default='', max_length=30),
        ),
    ]