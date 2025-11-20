from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from .forms import Registro


def registro(request):
    if request.method == "POST":
        form = Registro(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request,user)
            messages.success(request, f'bienvenido, {user.username}')
            return redirect('inicio')
    else:
        form = Registro()

    return render(request, 'pagina_finanzas/registro.html', {'form': form})
    
       
def InicioSesion(request):
    if request.method == "POST":
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                auth_login(request,user)
                return redirect('inicio')
    else:
        form = AuthenticationForm()
        
    return render(request, 'pagina_finanzas/InicioSesion.html',{'form':form})

def inicio(request):
    return render(request, 'pagina_finanzas/inicio.html')
