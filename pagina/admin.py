from django.contrib import admin
from .models import Cpu, Socket
# Register your models here.
@admin.register(Cpu)
class CpuAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock', 'frecuencia', 'turbo', 'nucleos', 'hilos', 'socket_id', 'graficos', 'cache', 'manufactura', 'tdp', 'nucleo')
    search_fields = ('nombre', 'precio', 'stock', 'frecuencia', 'turbo', 'nucleos', 'hilos', 'socket_id', 'graficos', 'cache', 'manufactura', 'tdp', 'nucleo')
    list_filter = ('nombre', 'precio', 'stock', 'frecuencia', 'turbo', 'nucleos', 'hilos', 'socket_id', 'graficos', 'cache', 'manufactura', 'tdp', 'nucleo')
    fieldsets = (
        ('Información general', {
            'fields': ('nombre', 'precio', 'stock', 'imagen')
        }),
        ('Especificaciones', {
            'fields': ('frecuencia', 'turbo', 'nucleos', 'hilos', 'socket_id', 'graficos', 'cache', 'manufactura', 'tdp', 'nucleo')
        }),
    )
admin.site.register(Socket)
