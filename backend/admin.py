from django.contrib import admin
from .models import AboutUsIntro, CategoryMonth, CategoryMonthTitle, Post, Carusel

admin.site.register(Post)
admin.site.register(Carusel)
admin.site.register(CategoryMonthTitle)
admin.site.register(CategoryMonth)
admin.site.register(AboutUsIntro)