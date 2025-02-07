from django.urls import path
from blogapp import views

urlpatterns = [path("", views.blog), path("exemplo/", views.exemploblog)]
