from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def admin(request):
    return render(request, 'admin.html', {})

def cart(request):
    return render(request, 'cart.html', {})

@login_required
def perfil(request):
    return render(request, 'perfil.html', {})

def producto(request):
    return render(request, 'producto.html', {})

def registrarse(request):
    return render(request, 'registrarse.html', {})

def loginV(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
    else:
        return redirect('login')

def logoutV(request):
    logout(request)
    return redirect('index')