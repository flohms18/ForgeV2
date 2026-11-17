from django.urls import path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("a-propos/", views.about, name="about"),
    path("projets/<slug:slug>/", views.project_detail, name="project_detail"),
    # L'ancienne page /articles/ redirige vers la liste sur l'accueil
    path("articles/", RedirectView.as_view(url="/#articles", permanent=True)),
    path("articles/<slug:slug>/", views.post_detail, name="post_detail"),
]
