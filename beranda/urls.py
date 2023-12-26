from django.urls import path
from . import views

urlpatterns = [
    path('', views.beranda, name='beranda'),
    path('menu/', views.menu, name='menu'),
]