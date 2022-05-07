from django.views.generic import *
from .models import *

class HomeView(ListView):
    template_name = "home.html"
    queryset = Carusel.objects.all()
    context_object_name = "carusels"


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
