from django.contrib import admin
from .models import AboutUsIntro, CategoryMonth, CategoryMonthTitle, OurServices, Post, Carusel

admin.site.register(Post)
admin.site.register(Carusel)
admin.site.register(CategoryMonthTitle)
admin.site.register(CategoryMonth)
admin.site.register(AboutUsIntro)
admin.site.register(OurServices)