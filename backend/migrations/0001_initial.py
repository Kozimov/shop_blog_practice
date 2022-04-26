# Generated by Django 4.0.4 on 2022-04-26 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('size', models.CharField(blank=True, max_length=20, null=True)),
                ('price', models.IntegerField(default=0)),
                ('image', models.ImageField(blank=True, null=True, upload_to='rasmlar/')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
    ]
