from django.db import models

class Post(models.Model):
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


    name = models.CharField(max_length=20, null=True, blank=True)
    size = models.CharField(max_length=20, null=True, blank=True)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to="rasmlar/", null=True, blank=True)

    def __str__(self):
        return str(self.name)