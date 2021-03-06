# Generated by Django 3.0.6 on 2020-09-07 22:52

import django.core.files.storage
from django.db import migrations, models
import src.contrib.validators
import src.apps.trainings.models.network


class Migration(migrations.Migration):

    dependencies = [
        ('trainings', '0006_auto_20200817_0243'),
    ]

    operations = [
        migrations.AddField(
            model_name='network',
            name='model_zip_file',
            field=models.FileField(blank=True, help_text='Url to download zipped network model file with also tensorflow weights.', max_length=200, storage=django.core.files.storage.FileSystemStorage(base_url='/media/networks/', location='/data/networks'), upload_to=src.apps.trainings.models.network.upload_network_zip_to, validators=[
                src.contrib.validators.FileValidator(content_types=['application/zip'], max_size=1610612736.0)], verbose_name='model zip file url'),
        ),
    ]
