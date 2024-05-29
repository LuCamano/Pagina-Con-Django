from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UsuarioTMManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El email es obligatorio')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('es_admin', True)
        return self.create_user(email, password, **extra_fields)


class UsuarioTM(AbstractBaseUser):
    '''
    Modelo personalizado de usuario
    '''
    email = models.EmailField('Ingresar correo', unique=True)
    nombre = models.CharField('Nombre',max_length=50, null=False, blank=False)
    apellido = models.CharField('Apellido',max_length=50, null=False, blank=False)
    direccion = models.CharField('Dirección',max_length=200, null=False, blank=False)
    telefono = models.IntegerField('Teléfono', null=False, blank=False)
    imagen = models.ImageField('Imagen de perfil', upload_to='usuarios', null=True, blank=True)
    run = models.CharField('Rut',max_length=10, unique=True, primary_key=True)  # Rol Único Tributario
    es_admin = models.BooleanField(default=False)
    # Agrega otros campos personalizados según tus necesidades

    # Define el campo que se utilizará para la autenticación
    USERNAME_FIELD = 'email'

    # Agrega otros campos requeridos para el modelo de usuario
    REQUIRED_FIELDS = ['nombre', 'apellido', 'direccion', 'telefono', 'run']

    # Define un manager personalizado para el modelo de usuario
    objects = UsuarioTMManager()

    def __str__(self):
        '''
        Retorna el run del usuario
        '''
        return self.run
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    def get_full_name(self):
        '''
        Retorna el nombre completo del usuario
        '''
        return f'{self.nombre} {self.apellido}'
    
    @property
    def is_staff(self):
        return self.es_admin