from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import PerfilUsuario, Gasto, Ingreso, Ahorro, CategoriaGasto


class Registro(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
        
        
class PerfilForm(forms.ModelForm):
    class Meta:
        model = PerfilUsuario
        fields = ['nombre_completo', 'telefono', 'direccion', 'fecha_nacimiento']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
            'direccion': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Ingresa tu dirección completa'}),
        }
        labels = {
            'nombre_completo': 'Nombre Completo',
            'telefono': 'Teléfono',
            'direccion': 'Dirección',
            'fecha_nacimiento': 'Fecha de Nacimiento',
        }

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = CategoriaGasto
        fields = ['nombre', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Ej: Comida, Transporte, Entretenimiento'}),
            'descripcion': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Descripción de la categoría'}),
        }

class GastoForm(forms.ModelForm):
    class Meta:
        model = Gasto
        fields = ['categoria', 'monto', 'descripcion', 'fecha']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'monto': forms.NumberInput(attrs={'placeholder': '0.00', 'step': '0.01'}),
            'descripcion': forms.TextInput(attrs={'placeholder': '¿En qué gastaste?'}),
        }
        labels = {
            'categoria': 'Categoría del Gasto',
            'monto': 'Monto Gastado ($)',
            'descripcion': 'Descripción',
            'fecha': 'Fecha del Gasto',
        }

class IngresoForm(forms.ModelForm):
    class Meta:
        model = Ingreso
        fields = ['monto', 'fuente', 'descripcion', 'fecha']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'monto': forms.NumberInput(attrs={'placeholder': '0.00', 'step': '0.01'}),
            'fuente': forms.TextInput(attrs={'placeholder': 'Ej: Salario, Negocio, Regalo'}),
            'descripcion': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Detalles del ingreso'}),
        }
        labels = {
            'monto': 'Monto Recibido ($)',
            'fuente': 'Fuente de Ingreso',
            'descripcion': 'Descripción',
            'fecha': 'Fecha del Ingreso',
        }

class AhorroForm(forms.ModelForm):
    class Meta:
        model = Ahorro
        fields = ['objetivo', 'monto_objetivo', 'monto_actual', 'fecha_limite']
        widgets = {
            'fecha_limite': forms.DateInput(attrs={'type': 'date'}),
            'monto_objetivo': forms.NumberInput(attrs={'placeholder': 'Monto que quieres ahorrar'}),
            'monto_actual': forms.NumberInput(attrs={'placeholder': 'Monto que ya tienes ahorrado'}),
            'objetivo': forms.TextInput(attrs={'placeholder': 'Ej: Viaje, Carro, Casa'}),
        }
        labels = {
            'objetivo': 'Objetivo de Ahorro',
            'monto_objetivo': 'Monto Objetivo ($)',
            'monto_actual': 'Monto Actual ($)',
            'fecha_limite': 'Fecha Límite',
        }