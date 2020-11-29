# Generated by Django 3.0.11 on 2020-11-29 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainings', '0012_auto_20201030_1959'),
    ]

    operations = [
        migrations.AddField(
            model_name='network',
            name='log_gamma_game_count',
            field=models.BigIntegerField(db_index=True, default=0, help_text='Number of real games used to compute log_gamma for this network.', verbose_name='log gamma game count'),
        ),
    ]
