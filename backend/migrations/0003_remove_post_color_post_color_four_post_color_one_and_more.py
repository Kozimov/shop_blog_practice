# Generated by Django 4.0.4 on 2022-04-26 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_post_brand_post_color_post_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='color',
        ),
        migrations.AddField(
            model_name='post',
            name='color_four',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='color_one',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='color_three',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='color_two',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
