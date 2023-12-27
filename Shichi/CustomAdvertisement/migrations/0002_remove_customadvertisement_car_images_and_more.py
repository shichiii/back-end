# Generated by Django 4.2.6 on 2023-12-27 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CustomAdvertisement', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customadvertisement',
            name='car_images',
        ),
        migrations.AddField(
            model_name='customadvertisement',
            name='car_image1',
            field=models.ImageField(blank=True, upload_to='car_images/'),
        ),
        migrations.AddField(
            model_name='customadvertisement',
            name='car_image2',
            field=models.ImageField(blank=True, upload_to='car_images/'),
        ),
        migrations.AddField(
            model_name='customadvertisement',
            name='car_image3',
            field=models.ImageField(blank=True, upload_to='car_images/'),
        ),
    ]
