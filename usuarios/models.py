from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UsuarioTM(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    password = models.CharField(max_length=128)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    run = models.CharField(max_length=12, unique=True)  # Rol Único Tributario
    # Agrega otros campos personalizados según tus necesidades

    # Define el campo que se utilizará para la autenticación
    USERNAME_FIELD = 'email'

    # Agrega otros campos requeridos para el modelo de usuario
    REQUIRED_FIELDS = ['first_name', 'last_name', 'direccion', 'telefono', 'run', 'password']

    # Define un manager personalizado para el modelo de usuario
    objects = BaseUserManager()