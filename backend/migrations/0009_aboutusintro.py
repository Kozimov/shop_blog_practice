# Generated by Django 4.0.4 on 2022-05-12 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_categorymonthtitle_remove_categorymonth_text_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUsIntro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('text', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='rasmlar/')),
            ],
        ),
    ]
