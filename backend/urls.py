from django.urls import path
from backend.views import AboutView, ContactView, HomeView, PostListView, ShopSingleView


urlpatterns = [
    path('', HomeView.as_view()),
    path('about/', AboutView.as_view(), name="about"),
    path('contact/', ContactView.as_view(), name="contact"),
    path('shop-single/', ShopSingleView.as_view(), name="shop-single"),
    path('shop/', PostListView.as_view(), name="shop"),
]
