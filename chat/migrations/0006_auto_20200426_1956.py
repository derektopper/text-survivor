# Generated by Django 3.0.5 on 2020-04-26 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_vote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='room',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='chat.Room'),
        ),
        migrations.AlterField(
            model_name='vote',
            name='votee',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='vote',
            name='voter',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
