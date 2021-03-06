#from django.db import models

from djongo import models
from django import forms

#from djangotoolbox.fields import EmbeddedModelField


class OrdenDetalle(models.Model):
	productID = models.IntegerField()
	cantidad = models.IntegerField()

	class Meta:
		abstract = True

class Orden(models.Model):
	codigo = models.CharField(max_length=255)
	fecha = models.DateTimeField(auto_now_add=True)
	total = models.FloatField()
	#detalle =  ListField(EmbeddedModelField('OrdenDetalle'))
	detalle = models.ArrayModelField(
        model_container=OrdenDetalle,
    )

	class Meta:
		abstract = True

class UserReport(models.Model):
    userID = models.IntegerField()
    full_name = models.CharField(max_length=255)
    ordenes = models.ArrayModelField(
        model_container=Orden,
    )
