# Generated by Django 3.0.4 on 2020-03-30 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_auto_20200330_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='img',
            field=models.ImageField(upload_to='Images/'),
        ),
    ]