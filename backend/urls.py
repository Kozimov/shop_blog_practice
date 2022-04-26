from django.urls import path
from backend.views import AboutView, ContactView, HomeView, PostListView, PostShopSingleView

app_name = "shop"

urlpatterns = [
    path('', HomeView.as_view()),
    path('about/', AboutView.as_view(), name="about"),
    path('contact/', ContactView.as_view(), name="contact"),
    path('<int:pk>/', PostShopSingleView.as_view(), name="shop-single"),
    path('shop/', PostListView.as_view(), name="shop"),
]
