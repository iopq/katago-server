# Generated by Django 3.0.6 on 2020-09-21 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startposes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StartPosCumWeightOnly',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('cumulative_weight', models.FloatField(db_index=True, default=-1, help_text='Cumulative weight, for efficient random selection.', verbose_name='cumulative_weight')),
            ],
            options={
                'db_table': 'startposes_startpos',
                'managed': False,
            },
        ),
        migrations.AlterField(
            model_name='startpos',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='creation date'),
        ),
        migrations.AlterModelTable(
            name='startpos',
            table='startposes_startpos',
        ),
    ]
