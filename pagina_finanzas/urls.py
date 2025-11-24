from django.urls import path
from django.views.generic import RedirectView
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', RedirectView.as_view(url='/inicio', permanent=True)),  
    path('inicio', views.inicio, name='inicio'),
    path('InicioSesion/', views.InicioSesion, name='InicioSesion'),
    path('Registro/', views.registro, name='Registro'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('perfil/', views.perfil, name='perfil'),
    path('gasto/nuevo/', views.agregar_gasto, name='agregar_gasto'),
    path('ingreso/nuevo/', views.agregar_ingreso, name='agregar_ingreso'),
]
