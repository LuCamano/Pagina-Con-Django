from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

User = get_user_model()

class FormularioRegistroUsuarioTM(UserCreationForm):
    password1 = forms.CharField(label='Contraseña',widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Contraseña',
            'id': 'password1',
            'required': 'required',
        }))
    password2 = forms.CharField(label='Confirmar contraseña',widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Reingresar contraseña',
            'id': 'password2',
            'required': 'required',
        }))
    class Meta:
        model = User
        fields = ['email', 'nombre', 'apellido', 'direccion', 'telefono', 'run']
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Correo electrónico',
                    'id': 'email',
                    'required': 'required',
                }),
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre',
                    'id': 'nombre',
                    'required': 'required',
                }),
            'apellido': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Apellido',
                    'id': 'apellido',
                    'required': 'required',
                }),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Dirección',
                    'id': 'direccion',
                    'required': 'required',
                }),
            'telefono': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Teléfono',
                    'id': 'telefono',
                    'required': 'required',
                }),
            'run': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Rut',
                    'id': 'run',
                    'required': 'required',
                }),
        }
