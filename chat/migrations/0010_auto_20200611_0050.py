# Generated by Django 3.0.5 on 2020-06-11 00:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0009_player_bounty'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='receiver',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='chat.Player'),
        ),
        migrations.AlterField(
            model_name='message',
            name='player',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='player', to='chat.Player'),
        ),
    ]