from django.urls import path
from . import views

urlpatterns = [
    path('', views.beranda, name='home'),
    path('home/', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

]