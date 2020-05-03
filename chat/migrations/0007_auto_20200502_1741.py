# Generated by Django 3.0.5 on 2020-05-02 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0006_auto_20200426_1956'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='game_round',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='vote',
            name='game_round',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='vote',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.Room'),
        ),
        migrations.AlterField(
            model_name='vote',
            name='votee',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='vote',
            name='voter',
            field=models.CharField(max_length=30),
        ),
    ]