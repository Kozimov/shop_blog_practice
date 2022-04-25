from django.urls import path
from backend.views import AboutView, ContactView, HomeView, ShopView


urlpatterns = [
    path('', HomeView.as_view()),
    path('about/', AboutView.as_view(), name="about"),
    path('shop/', ShopView.as_view(), name="shop"),
    path('contact/', ContactView.as_view(), name="contact"),
]
