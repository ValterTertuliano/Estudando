from django.urls import path
from blogapp import views

urlpatterns = [path("", views.blog, name='blog'), path("exemplo/", views.exemploblog, name='exemplo')]
