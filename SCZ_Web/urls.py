from django.urls import path
from SCZ_Web import views

urlpatterns= [
    path('', views.login),
    path('login',views.login),
    path('index',views.index),
    path('home',views.home)
]
