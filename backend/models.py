from django.db import models

class Post(models.Model):
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


    name = models.CharField(max_length=20, null=True, blank=True)
    size_one = models.CharField(max_length=20, null=True, blank=True)
    size_two = models.CharField(max_length=20, null=True, blank=True)
    size_three = models.CharField(max_length=20, null=True, blank=True)
    size_four = models.CharField(max_length=20, null=True, blank=True)
    brand = models.CharField(max_length=20, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    color = models.CharField(max_length=100, null=True, blank=True)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to="rasmlar/", null=True, blank=True)


    def __str__(self):
        return str(self.name)