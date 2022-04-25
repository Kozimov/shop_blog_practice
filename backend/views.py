from django.shortcuts import render
from django.views.generic import *


class HomeView(TemplateView):
    template_name = "home.html"

class AboutView(TemplateView):
    template_name = "about.html"

class ShopView(TemplateView):
    template_name = "shop.html"

class ContactView(TemplateView):
    template_name = "contact.html"
