from django.db import models

# Create your models here. 

class Producto(models.Model):
    '''
    Modelo de producto
    '''
    nombre = models.CharField('Nombre',max_length=100, null=False, blank=False)
    descripcion = models.CharField('Descripción',max_length=200, null=True, blank=True)
    precio = models.IntegerField('Precio', null=False, blank=False)
    stock = models.IntegerField('Stock', null=False, blank=False)
    imagen = models.ImageField('Imagen de producto', upload_to='productos', null=True, blank=True)
    # Agrega otros campos personalizados según tus necesidades
    
    def __str__(self):
        return self.nombre
    

class Socket(models.Model):
    '''
    Modelo de socket
    '''
    nombre = models.CharField('Nombre',max_length=100, null=False, blank=False)
    # Agrega otros campos personalizados según tus necesidades

    
    def __str__(self):
        return self.nombre
class Cpu(Producto):
    '''
    Modelo de CPU
    '''
    frecuencia = models.FloatField('Frecuencia', null=False, blank=False)
    turbo = models.FloatField('Frecuencia turbo', null=False, blank=False)
    nucleos = models.IntegerField('Núcleos', null=False, blank=False)
    hilos = models.IntegerField('Hilos', null=False, blank=False)
    socket_id = models.ForeignKey("pagina.Socket", verbose_name='Socket', on_delete=models.PROTECT, null=False, blank=False)
    graficos = models.CharField('Gráficos integrados', max_length=100, null=False, blank=False)
    cache = models.CharField("Caché", max_length=100, null=False, blank=False)
    manufactura = models.CharField('Manufactura', max_length=50, null=False, blank=False)
    tdp = models.IntegerField('TDP', null=False, blank=False)
    nucleo = models.CharField('Núcleo', max_length=50, null=False, blank=False)
    # Agrega otros campos personalizados según tus necesidades
