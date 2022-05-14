from django.contrib import admin
from .models import AboutUsIntro, Category, CategoryMonth, CategoryMonthTitle, OurBrandsImage, OurBrandsTitle, OurServiceCard, OurServiceTitle, Post, Carusel

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Carusel)
admin.site.register(CategoryMonthTitle)
admin.site.register(CategoryMonth)
admin.site.register(AboutUsIntro)
admin.site.register(OurServiceTitle)
admin.site.register(OurServiceCard)
admin.site.register(OurBrandsTitle)
admin.site.register(OurBrandsImage)