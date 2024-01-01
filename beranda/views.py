from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Home, Menu

def login(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def beranda(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def home(request):
    data = Home.objects.all()
    template = loader.get_template('home.html')
    context ={
        'menu': 'Macam-Macam jenis Makanan dan minuman yang tersedia di Pyog Cafe ',
        'home' : data
    }
    return HttpResponse(template.render(context, request))
    
def menu(request):
    data = Menu.objects.all()
    template = loader.get_template('menu.html')
    context ={
        'list' : "Macam-Macam Menu dan Deskripsi :",
        'menu' : data
    }
    return HttpResponse(template.render(context, request))

def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())

def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render())
