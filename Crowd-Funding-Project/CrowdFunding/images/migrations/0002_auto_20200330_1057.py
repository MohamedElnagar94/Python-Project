# Generated by Django 3.0.4 on 2020-03-30 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='img',
            field=models.CharField(max_length=100),
        ),
    ]