from django.views.generic import *
from .models import *

class HomeView(TemplateView):
    template_name = "home.html"

class AboutView(TemplateView):
    template_name = "about.html"
    
class ContactView(TemplateView):
    template_name = "contact.html"

class PostListView(ListView):
    template_name = "shop.html"
    queryset = Post.objects.all()
    context_object_name = "posts"
