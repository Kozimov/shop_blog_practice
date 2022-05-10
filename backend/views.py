from django.views.generic import *
from .models import *

class HomeView(ListView):
    template_name = "home.html"
    

    def get_queryset(self):
        return Carusel.objects.all()

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        # here we can add so many context using that way
        context['carusels'] = Carusel.objects.all()
        context['categoryMonthsTitles'] = CategoryMonthTitle.objects.all()
        context['categoryMonths'] = CategoryMonth.objects.all()

        return context


class AboutView(TemplateView):
    template_name = "about.html"
    
class ContactView(TemplateView):
    template_name = "contact.html"

class PostShopSingleView(DetailView):
    template_name = "shop-single.html"
    queryset = Post.objects.all()
    context_object_name = "post"

class PostListView(ListView):
    template_name = "shop.html"
    queryset = Post.objects.all()
    context_object_name = "posts"
