from django.urls import path
from . import views

urlpatterns = [
    path("", views.blogapp),
    path("exemplo1", views.exemplo_url_aninhada),
]
