from django.contrib import admin
from .models import CategoryMonth, Post, Carusel

admin.site.register(Post)
admin.site.register(Carusel)
admin.site.register(CategoryMonth)