# Generated by Django 3.0.11 on 2020-11-29 07:43

from django.db import migrations, models
import src.apps.runs.models.run


class Migration(migrations.Migration):

    dependencies = [
        ('runs', '0008_auto_20201129_0223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='run',
            name='rating_game_high_uncertainty_probability',
            field=models.FloatField(default=1.0, help_text='RELATIVE probability for high uncertainty rating game.', validators=[src.apps.runs.models.run.validate_non_negative], verbose_name='Rating game high uncertainty weight'),
        ),
    ]
