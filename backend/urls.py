from django.urls import path
from backend.views import AboutView, HomeView


urlpatterns = [
    path('', HomeView.as_view()),
    path('about/', AboutView.as_view(), name="about"),
]
