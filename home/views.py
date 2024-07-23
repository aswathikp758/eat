from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.
# from register.models import reg
from django.views.decorators.cache import cache_control

def index(request):
      return render(request,'index.html')

def index2(request):
    id = request.session['id']
    name = request.session['name']
    return render(request, 'index2.html', {'id': id, 'name': name})
    # return render(request,'index2.html')


def menu(request):
    return render(request, 'menu.html')


def about(request):
    return render(request, 'about.html')


