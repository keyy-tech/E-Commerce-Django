from django.urls import path, reverse_lazy
from . import views


urlpatterns = [
    path("home/", views.home, name="home"),
]
