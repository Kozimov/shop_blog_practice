# Generated by Django 4.0.4 on 2022-05-13 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0016_ourbrandstitle'),
    ]

    operations = [
        migrations.CreateModel(
            name='OurBrandsImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='rasmlar/')),
            ],
        ),
    ]
