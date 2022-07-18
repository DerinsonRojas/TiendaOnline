from re import T
from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=50, verbose_name="La dirección")
    email=models.EmailField()
    telefono=models.CharField(max_length=10, blank=True, null=True)

class Articulos(models.Model):
    nombre=models.CharField(max_length=30)
    seccion=models.CharField(max_length=20)
    precio=models.FloatField()

    def __str__(self):
        return 'El nombre es %s, la sección es %s y el precio es %s'% (self.nombre, self.seccion, self.precio)

class Pedidos(models.Model):
    numero=models.ImageField()
    fecha=models.DateField()
    entregado=models.BooleanField()
    
     
