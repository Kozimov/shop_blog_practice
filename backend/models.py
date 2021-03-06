from django.db import models
from .validators import validate_file_extension


class Category(models.Model):
    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'

    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)

class Post(models.Model):
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Postlar'

    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
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
    class Meta:
        verbose_name = "Oyning eng yaxshi to'plami sarlavhasi"
        verbose_name_plural = "Oyning eng yaxshi to'plami sarlavhasi"

    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)

    def __str__(self):
        return str(self.title)

class CategoryMonth(models.Model):
    class Meta:
        verbose_name = "Oyning eng yaxshi to'plami Post"
        verbose_name_plural = "Oyning eng yaxshi to'plami Postlari"

    image = models.ImageField(upload_to="rasmlar/")
    imageTitle = models.CharField(max_length=255)
    buttonText = models.CharField(max_length=255)

    def __str__(self):
        return str(self.imageTitle)


class AboutUsIntro(models.Model):
    class Meta:
        verbose_name = "Biz haqimizda kirish qismi"
        verbose_name_plural = "Biz haqimizda kirish qismlari"

    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    image = models.FileField(validators=[validate_file_extension], upload_to="rasmlar/")

    def __str__(self):
        return str(self.title)

class OurServiceTitle(models.Model):
    class Meta:
        verbose_name = "Bizning xizmatlar sarlavhasi"
        verbose_name_plural = "Bizning xizmatlar sarlavhasi"

    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)

    def __str__(self):
        return str(self.title)

class OurServiceCard(models.Model):
    class Meta:
        verbose_name = "Bizning xizmatlar sarlavhasi malumot qismi"
        verbose_name_plural = "Bizning xizmatlar sarlavhasi malumot qismlari"

    textIcon = models.CharField(max_length=255)
    text = models.CharField(max_length=255)

    def __str__(self):
        return str(self.text)

class OurBrandsTitle(models.Model):
    class Meta:
        verbose_name = "Bizning hamkorlar sarlavhasi"
        verbose_name_plural = "Bizning hamkorlar sarlavhasi"

    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)

    def __str__(self):
        return str(self.title)

class OurBrandsImage(models.Model):
    class Meta:
        verbose_name = "Bizning hamkorlar brandi"
        verbose_name_plural = "Bizning hamkorlar brandlari"

    image = models.ImageField(upload_to="rasmlar/")

    def __str__(self):
        return str(self.image)