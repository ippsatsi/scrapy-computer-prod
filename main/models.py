from django.db import models
from django.utils import timezone
# Create your models here.

from django.utils import timezone

class Quote(models.Model):
    """
    The scrapped data will be saved in this model
    """
    text = models.TextField()
    author = models.CharField(max_length=512)
    fecha = models.DateField(default=timezone.now)


class Producto(models.Model):

    titulo = models.TextField(max_length=512)
    precio_soles = models.FloatField(blank= True, null= True)
    precio_dolares = models.FloatField(blank= True, null= True)
    categoria = models.TextField(max_length=30)
    marca = models.TextField(max_length=20)
    proveedor = models.TextField(max_length=30)
    fecha = models.DateField(default=timezone.now)