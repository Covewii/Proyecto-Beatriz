from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from .forms import Registro, PerfilForm, GastoForm, IngresoForm

def registro(request):
    if request.method == "POST":
        form = Registro(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, f'bienvenido, {user.username}')
            return redirect('inicio')
    else:
        form = Registro()
    return render(request, 'pagina_finanzas/registro.html', {'form': form})

def InicioSesion(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('inicio')
    else:
        form = AuthenticationForm()
    return render(request, 'pagina_finanzas/InicioSesion.html', {'form': form})

def inicio(request):
    return render(request, 'pagina_finanzas/inicio.html')

def perfil(request):
    if request.method == "POST":
        form = PerfilForm(request.POST)
        if form.is_valid():
            perfil = form.save(commit=False)
            perfil.usuario = request.user
            perfil.save()
            return redirect('inicio')
    else:
        form = PerfilForm()
    return render(request, 'pagina_finanzas/perfil.html', {'form': form})

def agregar_gasto(request):
    if request.method == "POST":
        form = GastoForm(request.POST)
        if form.is_valid():
            gasto = form.save(commit=False)
            gasto.usuario = request.user
            gasto.save()
            return redirect('inicio')
    else:
        form = GastoForm()
    return render(request, 'pagina_finanzas/agregar_gasto.html', {'form': form})

def agregar_ingreso(request):
    if request.method == "POST":
        form = IngresoForm(request.POST)
        if form.is_valid():
            ingreso = form.save(commit=False)
            ingreso.usuario = request.user
            ingreso.save()
            return redirect('inicio')
    else:
        form = IngresoForm()
    return render(request, 'pagina_finanzas/agregar_ingreso.html', {'form': form})