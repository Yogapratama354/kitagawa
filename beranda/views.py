from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Beranda, Menu

def beranda(request):
    template = loader.get_template('beranda.html')
    return HttpResponse(template.render())

def menu(request):
    template = loader.get_template('menu.html')
    return HttpResponse(template.render())


