from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import FormularioRegistroUsuarioTM

# Create your views here.

def registrarse(request):
    if request.method == 'POST':
        form = FormularioRegistroUsuarioTM(request.POST)
        if form.is_valid():
            form.save()
            print('Usuario creado correctamente')
            return redirect('login')
        print('Error al crear el usuario')
        print(form.error_messages)
    else:
        form = FormularioRegistroUsuarioTM()
    return render(request, 'registrarse.html', {'form': form})

def loginV(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return redirect('login')
    else:
        return render(request, 'login.html', {})

def logoutV(request):
    logout(request)
    return redirect('index')