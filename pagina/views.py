from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

@login_required
def admin(request):
    return render(request, 'admin.html', {})

def cart(request):
    return render(request, 'cart.html', {})

@login_required
def perfil(request):
    return render(request, 'perfil.html', {})

def producto(request):
    return render(request, 'producto.html', {})

