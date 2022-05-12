from django.db import models
from .validators import validate_file_extension


class Post(models.Model):
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Postlar'


    name = models.CharField(max_length=20, null=True, blank=True)
    size_one = models.CharField(max_length=20, null=True, blank=True)
    size_two = models.CharField(max_length=20, null=True, blank=True)
    size_three = models.CharField(max_length=20, null=True, blank=True)
    size_four = models.CharField(max_length=20, null=True, blank=True)
    brand = models.CharField(max_length=20, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    color = models.CharField(max_length=100, null=True, blank=True)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to="rasmlar/", null=True, blank=True)


    def __str__(self):
        return str(self.name)


class Carusel(models.Model):
    class Meta:
        verbose_name = "Karusel"
        verbose_name_plural = "Karusellar"

    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    image = models.ImageField(upload_to="rasmlar/")

    def __str__(self):
        return str(self.name)

class CategoryMonthTitle(models.Model):
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)

    def __str__(self):
        return str(self.title)

class CategoryMonth(models.Model):
    image = models.ImageField(upload_to="rasmlar/")
    imageTitle = models.CharField(max_length=255)
    buttonText = models.CharField(max_length=255)

    def __str__(self):
        return str(self.imageTitle)


class AboutUsIntro(models.Model):
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    image = models.FileField(validators=[validate_file_extension], upload_to="rasmlar/")
