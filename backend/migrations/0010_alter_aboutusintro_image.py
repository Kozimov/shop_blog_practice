# Generated by Django 4.0.4 on 2022-05-12 04:54

import backend.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0009_aboutusintro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutusintro',
            name='image',
            field=models.FileField(upload_to='rasmlar/', validators=[backend.validators.validate_file_extension]),
        ),
    ]
