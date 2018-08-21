#from django.db import models
from django.db import models

from djangotoolbox.fields import EmbeddedModelField

# Create your models here.

class OrdenDetalle(models.Model):
	productID = models.IntegerField()
	productName = models.CharField(max_length=255)
	cantidad = models.IntegerField()

class Orden(models.Model):
	codigo = models.CharField(max_length=255)
	fecha = models.DateTimeField(auto_now_add=True)
	total = models.FloatField()
	detalle =  ListField(EmbeddedModelField('OrdenDetalle'))

class ReporteDeCompras(models.Model):
    userID = models.IntegerField()
    full_name = models.CharField(max_length=255)
    ordenes = ListField(EmbeddedModelField('Orden'))