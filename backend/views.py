from django.shortcuts import reverse
from django.views.generic import *

from backend.forms import NewUserForm
from .models import *

class SignUpView(CreateView):
    template_name = "registration/signup.html"
    form_class = NewUserForm

    def get_success_url(self):
        return reverse("login")

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


class AboutView(ListView):
    template_name = "about.html"

    def get_queryset(self):
        return AboutUsIntro.objects.all()

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        # here we can add so many context using that way
        context['aboutUsIntros'] = AboutUsIntro.objects.all()
        context['ourServicesTitles'] = OurServiceTitle.objects.all()
        context['ourServicesCards'] = OurServiceCard.objects.all()
        context['ourBrandsTitles'] = OurBrandsTitle.objects.all()
        context['ourBrandsImages'] = OurBrandsImage.objects.all()

        return context
    
class ContactView(TemplateView):
    template_name = "contact.html"

class PostShopSingleView(DetailView):
    template_name = "shop-single.html"
    queryset = Post.objects.all()
    context_object_name = "post"

class PostListView(ListView):
    template_name = "shop.html"

    def get_queryset(self):
        return Post.objects.all()

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        # here we can add so many context using that way
        context['posts'] = Post.objects.all()
        context['categories'] = Category.objects.all()

        return context
