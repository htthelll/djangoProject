# Generated by Django 4.1 on 2023-08-14 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_image_marker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='marker',
            field=models.CharField(default='undefined', max_length=100),
        ),
    ]
