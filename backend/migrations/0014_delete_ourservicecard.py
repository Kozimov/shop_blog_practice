# Generated by Django 4.0.4 on 2022-05-12 05:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0013_ourservicetitle_rename_ourservice_ourservicecard_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OurServiceCard',
        ),
    ]
