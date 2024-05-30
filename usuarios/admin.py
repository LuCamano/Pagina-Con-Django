from django.contrib import admin
from .models import UsuarioTM

# Register your models here.
@admin.register(UsuarioTM)
class UsuarioTMAdmin(admin.ModelAdmin):
    list_display = ('email', 'nombre', 'apellido', 'direccion', 'telefono', 'run', 'es_admin')
    search_fields = ('email', 'nombre', 'apellido', 'direccion', 'telefono', 'run', 'es_admin')
    list_filter = ('email', 'nombre', 'apellido', 'direccion', 'telefono', 'run', 'es_admin')
    fieldsets = (
        ('Información general', {
            'fields': ('email', 'nombre', 'apellido', 'direccion', 'telefono', 'imagen', 'run', 'es_admin')
        }),
    )