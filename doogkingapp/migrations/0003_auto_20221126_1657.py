# Generated by Django 3.2.16 on 2022-11-26 16:57

from django.db import migrations, models
import django.db.models.deletion
import storages.backends.azure_storage


class Migration(migrations.Migration):

    dependencies = [
        ('doogkingapp', '0002_images_and_reset'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='housing',
            name='otp',
        ),
        migrations.AddField(
            model_name='housing',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.CreateModel(
            name='HousingImage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('index', models.IntegerField(default=0)),
                ('image', models.ImageField(default='default.svg', storage=storages.backends.azure_storage.AzureStorage, upload_to='')),
                ('housing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doogkingapp.housing')),
            ],
        ),
    ]
