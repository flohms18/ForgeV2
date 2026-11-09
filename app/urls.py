from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("a-propos/", views.about, name="about"),
    path("articles/", views.post_list, name="post_list"),
    path("articles/<slug:slug>/", views.post_detail, name="post_detail"),
]
