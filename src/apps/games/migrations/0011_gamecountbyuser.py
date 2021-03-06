# Generated by Django 3.0.6 on 2020-10-22 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0010_gamecountbynetwork'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameCountByUser',
            fields=[
                ('id', models.CharField(db_index=True, max_length=128, primary_key=True, serialize=False)),
                ('username', models.CharField(db_index=True, max_length=255)),
                ('total_num_training_games', models.IntegerField(db_index=True)),
                ('total_num_training_rows', models.IntegerField()),
                ('total_num_rating_games', models.IntegerField(db_index=True)),
            ],
            options={
                'db_table': 'games_gamecountbyuser',
                'managed': False,
            },
        ),
    ]
